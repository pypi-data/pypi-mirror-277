from ohmytofu.autobrew.trft.resolvers import (
    create_project_from_template,
    batch_ingest,
    trigger_pipeline
)
from ohmytofu.log import EvalError, EvalConfig, EvalStats, EvalResults, EvalMetric
from ohmytofu.connectivity.sse import handle_sse_events, listen_to_sse_stream
from ohmytofu.autobrew.trft.Subspace import PartitionConfig, Subspace
from ohmytofu.autobrew.trft.model import TrftModel
from ohmytofu.display._display import TaskProfile
from ohmytofu.utils.runtime import block
from ohmytofu.display import display
from datetime import datetime
from base64 import b64encode
from uuid import uuid4
import asyncio
import json
import os

API_BASE = 'https://db.tc.ohmytofu.ai'
READABLE_VALUETYPES = {
    'multipleChoice': 'Multiple Choice',
    'enum': 'Single Choice'
}

MANDATORY_ENV_KEYS = {
    'TOFU_API_KEY',
    'TOFU_WORKSHOP_ID',
    'TOFU_TEMPLATE_ID'
}

PROJECT_APIS = [{
    'name': 'Training',
    'pipeline': {'name': 'Trft Trainer', 'file': 'trft-train.py'},
    'trigger': {'name': 'Train Model', 'inputs': ['input']}
}]

PROJECT_DATASET = {
    'name': 'Training Dataset Simulatrex',
    'type': 'noconf',
    'uniqueIdColumn': 'Token',
    'partitionColumn': 'trainingID'
}
BATCH_COLUMN_IDENTIFIER = 'trainingID'
CONTACT_SUPPORT = "Please contact support@ohmytofu.ai if the issue persists."

class TrftTrainerException(Exception):
    pass

class TrftTrainer:
    """
    Finetunes a raft layer with the provided basemodel and dataset.

    Arguments:
        base_model                     (TofuHFModel): A huggingface transformer model (loaded via Tofu AI)
        subspace (transforms.autobrew.trft.Subspace): A Trft Subspace Partitioning Schema
        train_dataset             (pandas.DataFrame): A dataset that can be processed with the Subspace config (needs the correct columns defined in the subspace)
        model_name                          (String): Descripive name of this training run. This will help you find the model lateron.
        target_layer                           (int): Which layer to target
        num_rafts                              (int): How many rafts should intervene on this training?
    
    Example:
        >>> from transforms.autobrew.trft.Subspace import PartitionConfig, Subspace
        >>> from transforms.autobrew.trft.trainer import TrftTrainer
        >>> from transformers import AutoModelForCausalLM, AutoTokenizer
        >>> # setup the dataset partition config
        >>> pc = PartitionConfig(
        >>>    group_defining_columns=group_defining_columns,
        >>>    train_data_defining_columns=train_data_defining_columns,
        >>>    partition_at=partition_at
        >>> ) 
        >>>
        >>> # create a subspace with the config
        >>> subspace = Subspace(pc)
        >>> # load a transformer model TODO
        >>> base_model = 'mistralai/Mistral-7B-v0.2'
        >>> model = AutoModelForCausalLM(base_model)
        >>> tokenizer = AutoTokenizer(base_model)
        >>>
        >>> # load your dataset
        >>> df = pd.read_parquet(...)
        >>>
        >>> # setup the trainer
        >>> trainer = TrftTrainer(
        >>>             base_model=model,
        >>>             tokenizer=tokenizer,
        >>>             subspace=subspace,
        >>>             train_dataset=df,
        >>> ) 
        >>> # train the model
        >>> trainer.train()
        >>>             
        
    """
    def __init__(
            self,
            base_model,
            subspace,
            train_dataset,
            model_name        = None,
            target_layer      = 15,
            num_rafts         = 1,
            save_after_train  = True
    ):
        self.base_model       = base_model
        self.subspace         = subspace
        self.raw_dataset      = train_dataset
        self.target_layer     = target_layer
        self.num_rafts        = num_rafts
        self.save_after_train = save_after_train
        self.model_name       = model_name
        self.display_p        = None # holds the display
        self.display_t        = None # holds the display task context
        self.trainer_project  = None # holds data when requesting a new project

        # Sanity Check of the config - raise exception if config seems not Ok
        self.check_config_ok_or_raise()

    # helper
    def _build_dict(self, seq, key):
        return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

    def split_dataset_partition(self, dataset, group_name_key='name', debug_level=0):
        from pandas import DataFrame
        df_train = DataFrame(dataset)
        # holds our result
        ds_split = []
        # read config
        splitpoints     = self.subspace.config.splitpoint
        split_col       = splitpoints['column']
        split_data_type = splitpoints['dataType']
        split_groups    = splitpoints['groups']
        # sanity check the provided config
        if split_data_type != 'string': raise Exception("""Not implemented. Please use `dataType='string' for now.` """)
        
        if debug_level >=1: print(f""" 
split_data_type:      {split_data_type}
split_col:            {split_col}
split_groups:         {split_groups}
          """)
        # loop over the partitions to make 3 separate datasets
        for group in split_groups:
            # get the config for the group
            group_by_name = self._build_dict(split_groups, key=group_name_key)
            group_members = group_by_name[group['name']]['members']
            # TOOD: whenever we include `int`types this needs to update
            # filter the dataset for the group
            df_group = df_train[df_train[split_col].isin(group_members)]
            # add to results
            ds_split.append({ 'name': group['name'], 'data': df_group, 'split_col': split_col})

        return ds_split
    
    def preprocess_dataset_for_raft(self, dataset, partitioned=True):
        # assume we have a partitioned list of datasets from self.split_dataset_partition()
        assert partitioned, "not implemented - please use a partitioned dataset and set `partitioned=True`"
        assert type(dataset) == type([]), "Dataset seems wrong type. Should be partitioned list of datasets."
       
        preprocessed = []

        for raw_ds in dataset:
            partition_name = raw_ds['name']
            split_col      = raw_ds['split_col']
            # add the subspaces to the dataset
            raw_ds['data']['subspaces'] = raw_ds['data'][split_col].apply(lambda _: self.subspace.get_partition(partition_name))
            # save partition name for later
            raw_ds['data']['partition'] = partition_name

            preprocessed.append({'name': partition_name, 'dataset': raw_ds['data']})

        return preprocessed

    def _get_config_kv(self, seq, key='validOptions', col_identifier='columnName'):
        # filter invalid entries
        valid_seq = [d for d in seq if key in d]
        return dict((d[col_identifier], d[key]) for (index, d) in enumerate(valid_seq))


    def _postprocess_ds(self, ds):
        """
        Builds a instruction dynamically with the provided subspace schema.
        """
        # build the template
        template = """{group_def_template}\n{question}. ({value_type}, Options: {options}):""" 

        # get dicts of question answer pairs
        group_def_data = [{item: ds[item]} for item in self.subspace.config.group]
        # join them to a string
        group_def_template = '\n'.join([f"{key}: {value}" for d in group_def_data for key, value in d.items()])

        # read the value type and translate it to a human readable form
        value_type_cfg = self._get_config_kv(seq=self.subspace.config.train, key='valueType')[ds['question']]
        # get the human readable form, if not possible just pass on what was in the config
        value_type = READABLE_VALUETYPES.get(value_type_cfg, value_type_cfg)

        # get valid options
        options = self._get_config_kv(seq=self.subspace.config.train, key='validOptions')[ds['question']]
        options_text = ', '.join(options)

        # format the instruction
        instruction = template.format(
            question=ds['question'],
            options=options_text,
            value_type=value_type,
            group_def_template=group_def_template,
        )
        return instruction

    def build_dataset(self, dataset_output_type='dataset', training_id=None):
        from pandas import concat, melt
        from datasets import Dataset

        # TODO check that we don't have objects, sets or arrays as a column

        # read splitpoint data and make a split dataset by partition
        ds_partitioned = self.split_dataset_partition(self.raw_dataset)
        # preprocess dataset to add subpartition for data collator
        ds_preprocessed = self.preprocess_dataset_for_raft(ds_partitioned) 
        # combine back to one dataset, the partitions are now expressed in the `subpartition` column
        subspace_dataset = concat([partitioned_dataset['dataset'] for partitioned_dataset in ds_preprocessed])
        # collect columns we want to have in every row of the training dataset
        keep = [col['columnName'] for col in self.subspace.config.train] + [col for col in self.subspace.config.group] 
        df_interest = subspace_dataset[keep]
        # keep these in every row
        cols_for_every_row = self.subspace.config.group
        # melt into simple questions
        # turn the multi column dataset into multiple rows, one for each question while keeping the columns defined in `keep`
        df_train = melt(df_interest, id_vars=cols_for_every_row, var_name="question", value_name="output", ignore_index=True) 

        # make an instruction from template and questio by applying the template
        df_train['instruction'] = df_train.apply(self._postprocess_ds, axis=1)
        # our trainer is using the Alpaca dataset format which has an input field, it can be empty though
        df_train['input'] = ''
        
        if training_id: df_train[BATCH_COLUMN_IDENTIFIER] = training_id

        if dataset_output_type == 'pandas': return df_train

        return Dataset.from_pandas(df_train)

    def _check_columns_exists(self, df, to_check):
        found = set(to_check).issubset(df.columns)
        if found: return True
        # Find missing columns
        missing_columns = [col for col in to_check if col not in df.columns]
        
        # If there are missing columns, print them and return False
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return False

    def _check_env(self):
        missing_keys = [key for key in MANDATORY_ENV_KEYS if key not in os.environ]
        # If there are missing keys, print them and return False
        if missing_keys:
            print(f"Missing keys: {missing_keys}")
            return False

        return True

    def check_config_ok_or_raise(self):
        # check columns exist
        columns_to_check = \
           [col['columnName'] for col in self.subspace.config.train] + \
           [col for col in self.subspace.config.group] + \
           [self.subspace.config.splitpoint['column']] + \
           [self.subspace.config.unique_id_column]

        config_valid = self._check_columns_exists(self.raw_dataset, columns_to_check)
        # check environment variables are set
        config_valid = self._check_env()

        if not(config_valid): raise Exception("config invalid")
        return True

    def _init_project_config(self):
        return {
            'name': self.model_name,
            'createDataLineage': [{
                **PROJECT_DATASET,
                'apis': PROJECT_APIS,
                'dataFields': [{
                    'name': field['columnName'],
                    'userSelectedType': field['dataType']
                } for field in self.subspace.config.train] + \
                [{
                  'name': 'trainingID',
                  'userSelectedType': 'meta'
                },{
                  'name': self.subspace.config.unique_id_column,
                  'userSelectedType': 'meta'
                }],
          }]
        }

    def _evaluate_state_message(self, msg):
        """
        Parses a state message for the following conditions:
        a) no errors
        b) all items True
        c) results not empty
        """
        # Helper function to check nested dictionaries
        def all_true(d):
            for key, value in d.items():
                if isinstance(value, dict):
                    if not all_true(value):
                        return False
                elif not value:
                    return False
            return True

        # Check if 'errors' is None, 'results' is not empty, and all entries in 'state' are True
        if msg.get('errors') is None and msg.get('results') and all_true(msg.get('state', {})):
            return True
        return False


    def _check_project_creation_complete(self, msg):
        state = msg['state']
        errors =  msg['errors'] if 'errors' in msg else None

        # stop on errors
        if errors: 
            # errors can be dict or string messages
            _errors = [ entry['error'] if type(entry) == dict else entry for entry in errors]
            raise Exception(f"""could not create your project due to {len(_errors)} Errors: {', '.join(_errors)}""")

        # if we're done this sends 'True' and closes the channel
        return self._evaluate_state_message(msg)

    def _handle_status_message(self, message, td, finish_prev_task=False, prev_task=None, total_steps=20, debug_level=0):
        # finish the previous task
        if finish_prev_task and prev_task: self._progress(
                prev_task['p'],
                name=prev_task['name'],
                n=prev_task['total_steps']+1
        )

        has_progress = 'progress' in message and 'total' in message
        is_update = 'isUpdate' in message and message['isUpdate'] == True
        is_done = 'module' in message and message['module'] == "ohmytofu.stageDone"
        step = None
        if has_progress: step = message['progress']
        else: print(f"noprogress msg: {message}")
        if is_done: return True
        if is_update: return self._progress(self.display_p, n=step if has_progress else None, name=message['status'])
        with self.display_t.progress(total=message['total'] if has_progress else None) as self.display_p:
            self._progress(self.display_p, n=step if has_progress else None, name=message['status'])
    def _handle_status_message_for_project_creation(self, message, td, finish_prev_task=False, prev_task=None, total_steps=20, debug_level=0):
        # Helper function to count total and true elements
        def count_elements(d):
            total = 0
            true_count = 0
            for key, value in d.items():
                if isinstance(value, dict):
                    nested_total, nested_true = count_elements(value)
                    total += nested_total
                    true_count += nested_true
                else:
                    total += 1
                    if value:
                        true_count += 1
            return total, true_count

        def get_total_and_progress(state):
            total_steps, true_steps = count_elements(state)
            return total_steps, true_steps

        # Helper function to find the first false (currently processed) element
        def find_first_false(d, path=""):
            for key, value in d.items():
                current_path = f"{path}/{key}" if path else key
                if isinstance(value, dict):
                    result = find_first_false(value, current_path)
                    if result:
                        return result
                elif not value:
                    return current_path
            return None
        
        if finish_prev_task and prev_task: self._progress(
                prev_task['p'],
                name=prev_task['name'],
                n=prev_task['total_steps']+1
        )

        # read the current state from the message
        state = message.get('state', {})
        next_todo = find_first_false(state)
        total, progress = get_total_and_progress(state)
        is_update = (progress != 0)
        is_done = (progress == total) and (next_todo == None) and message['results']
        status_message = f"Creating {next_todo}"

        if not(total) or not(progress): return

        if is_done:
            self.trainer_project = message['results']
            return True

        if is_update:
            return self._progress(
                self.display_p, n=progress, name=status_message if next_todo else 'Finalizing project setup'
            )
        # initiate a new progress display
        with td.progress(total=total) as self.display_p:
            self._progress(self.display_p, n=progress, name=parsed_message['status'])


    def _find_value_in_synced_config(self, value, key='userRequestedDataLineage'):
        return self.trainer_project[key][0][value]

    def _find_trigger_in_synced_config(self, key='userRequestedDataLineage'):
        return self.trainer_project[key][0]['trigger']

    async def display_progress(self, template_id, training_id, show_summary=True):
        def now ():
            return datetime.now().isoformat()

        # TODO
        eval_cfg = EvalConfig(
            epochs=1
        )
        # TODO
        start_timer = now()
        # TODO 
        total_steps = 11

        #  with display().task(profile) as self.display_t:
            # sync task (create project from template)
        with self.display_t.progress(total=total_steps) as p:
            self.display_p = p
            # initial task display
            task_name = 'Syncing'
            this_task = {'p': p, 'total_steps': total_steps, 'name': task_name}
            self._progress(p, name=task_name)

            # create project task progress
            on_msg_callback  = lambda msg: self._handle_status_message_for_project_creation(
                msg,
                td=self.display_t,
                prev_task=this_task,
                finish_prev_task=False,
                total_steps=total_steps
            )

            project_created_task_event = asyncio.create_task(
                listen_to_sse_stream(
                    template_id,
                    tofu_type="createprojectfromtemplate2",
                    on_message=on_msg_callback, # this closes the channel once true
                ) # todo: this needs to send the uuid instead of this template id
            )
            # wait for it to complete
            await project_created_task_event


            return True

    async def display_progress_stage_II(self, template_id, training_id, show_summary=True):
        # batch ingest task progress
        with self.display_t.progress(total=2) as p:
            self.display_p = p
            trainer_do, trained_models_do = self._find_dataobjects_in_synced_config()
            self._progress(p, name='ingest training data')
            batch_ingest_task_event = asyncio.create_task(
                handle_sse_events(
                    trainer_do['rid'],
                    tofu_type="dataObjectType",
                )
            )
            await batch_ingest_task_event
            self._progress(p, n=3, name='Ingest Training Data')
            return True

    async def display_progress_stage_III(
        self,
        trigger_id,
        training_id,
        show_summary=True,
        total_steps=100, 
        task_name='Acquiring GPU'
    ):

        # batch ingest task progress
        with self.display_t.progress(total=total_steps) as p:
            self.display_p = p
            trainer_do, trained_models_do = self._find_dataobjects_in_synced_config()
            self._progress(p, name=task_name)
            # setup a status message listener with callback
            this_task = {'p': p, 'total_steps': total_steps, 'name': task_name}
            # callback
            on_msg_callback  = lambda msg: self._handle_status_message(
                msg,
                td=self.display_t,
                prev_task=this_task,
                finish_prev_task=True
            )
            task_events = asyncio.create_task(
                listen_to_sse_stream(
                    trigger_id, 
                    tofu_type="triggerPipeline",
                    on_message=on_msg_callback,
                    debug_level=0
                )
            )
            await task_events

            return True

    def _progress(self, p, n=0, name="Task") -> None:
        p.update(n, name=name)

    def _find_project_api(self, api_name, key='dataLineage'):
        dataobjects = self.trainer_project[key][0]['dataObjects']
        return next((d for d in dataobjects if d['apiName'] == api_name), None)

    def _find_trained_models_workshop_in_synced_config(self):
        return next((d for d in self.trainer_project['applications'] if d['name'] == f'[{self.model_name}] Trained Models'), None)

    def _create_training_pipeline_config(self, training_id, encode='dict'):
        training_data_do, trained_models_do = self._find_dataobjects_in_synced_config()
        [p] = self._find_value_in_synced_config('pipeline')
        [t] = self._find_value_in_synced_config('trigger')
        [tdf] = t['settings']['datafields']

        config = {
            'name'          : self.model_name,
            'data'          : {
                'name'                          : self.model_name,
                'type'                          : 'noconf',
                'uniqueIdColumn'                : self.subspace.config.unique_id_column,
                'partitionColumn'               : self.subspace.config.splitpoint['column'],
            },
            'apis'          : {
                'name'                          : 'Training',
                'pipeline'                      : {'name': p['name'], 'file': p['fileName']},
                'trigger'                       : {'name': t['name'], 'inputs': [tdf['name']]},
            },
            'train'         : {
                'group_defining_columns'        : self.subspace.config.group,
                'train_data_defining_columns'   : self.subspace.config.train,
                'partition_at_single'           : self.subspace.config.splitpoint

            },
            'trainingID'    : training_id,
            'templateID'    : os.environ['TOFU_TEMPLATE_ID'],
            'dataRID'       : training_data_do['rid'],
            'dataID'        : training_data_do['id'],
            'targetRID'     : trained_models_do['rid'],
            'targetID'      : trained_models_do['id'],
        }

        # encode as b64 string for transport
        if encode == 'b64': return b64encode(json.dumps(config).encode()).decode('utf-8')
        assert encode == 'dict', 'encode should either be `dict` or `b64`'
        return config

    def _find_trainer_settings_in_synced_config(self, training_id):
        _, trained_models_do = self._find_dataobjects_in_synced_config()
        [trigger] = self._find_value_in_synced_config('trigger')
        # encode the complex object to a b64 string for transport
        trainer_settings = self._create_training_pipeline_config(training_id, encode="b64")
        datafields = [
            {
                'name': '**output_rid',
                'value': trained_models_do['rid']
            }, {
                'name': 'trainingID',
                'value': training_id
            }, {
                'name': 'trainingConfig',
                'value': trainer_settings
            }, {
                'name': 'apiKey',
                'value': os.environ['TOFU_API_KEY']
            }, {
                'name': 'apiBase',
                'value': API_BASE 
            },
            {
            'name': '**batch_trigger_id', # gives us an sse_logger
            'value': trigger['id']
            }
        ]
        return {'datafields': datafields}

    def _find_dataobjects_in_synced_config(self):
        trainer_do = self.trainer_project['userRequestedDataLineage'][0]['dataObjects'][0]
        trained_models_do = self._find_project_api('trainedModels')
        return trainer_do, trained_models_do

    def _now (self):
        return datetime.now().isoformat()
    @block
    async def train(self, num_train_epochs=100, lr=2e-3, logging_steps=500, batch_size=16, return_trained_model=True):
        from ohmytofu.connectivity.gqlclient import client as tofu_gql
        if not self.model_name:
            self.model_name = "{:New Model %Y-%m-%d-T%H-%M}".format(datetime.now())

        training_run_id = str(uuid4())
        template_id = os.environ['TOFU_TEMPLATE_ID']
        # prepare the dataset for training
        training_dataset = self.raw_dataset.copy()
        training_dataset.loc[:,BATCH_COLUMN_IDENTIFIER] = training_run_id

        eval_cfg = EvalConfig(
            epochs=1
        )
        # TODO
        start_timer = self._now()
        # TODO 
        total_steps = 11

        profile = TaskProfile(
            name=self.model_name,
            batch_id=training_run_id,
            sequence=[0,1],
            model="TofuAI",
            dataset="testDS",
            scorer="(none)",
            samples=len(training_dataset),
            eval_config=eval_cfg,
            log_location=None,
            task_args={},
            generate_config=None
        )
        with display().task(profile) as self.display_t:

            #  training_dataset =  self.build_dataset(
                #  dataset_output_type='pandas',
                #  training_id=training_run_id,
            #  )
            # set a timestamp as the model name if it was not supplied at trainer init
            # Sanity Check of the config - raise exception if config seems not Ok
            self.check_config_ok_or_raise()
            project_config = self._init_project_config()

            # TODO: make global display
            # tracks status updates sent from the API and displays them to the user
            progress_stage_I = asyncio.create_task(
                self.display_progress(template_id, training_run_id)
            )

            create_project_task = asyncio.create_task(
                create_project_from_template(template_id, project_config, tofu_gql)
            )
            # initiate project creation
            await create_project_task
            await progress_stage_I

            if not(self.trainer_project): raise TrftTrainerException(f'Project not found. {CONTACT_SUPPORT}')

            # ingest training data
            # find the IDs needed for the training from the config received
            trainer_do, trained_models_do = self._find_dataobjects_in_synced_config()
            _patched_rid_trainer_do = trainer_do['rid'].replace('_', '.')
            batch_ingest_params = {
                "rid": _patched_rid_trainer_do, # we're migrating away from the `_` syntax
                "primaryKey": "id",
                "data": training_dataset.to_dict(orient='records'),
            }
            # tracks status updates sent from the API and displays them to the user
            progress_stage_II = asyncio.create_task(
                self.display_progress_stage_II(template_id, training_run_id)
            )
            batch_ingest_task = asyncio.create_task(batch_ingest(batch_ingest_params, tofu_gql))
            await batch_ingest_task
            maybe_ingest_task_started = batch_ingest_task.result()
            ingest_accepted = maybe_ingest_task_started['batchIngestData'] if 'batchIngestData' in maybe_ingest_task_started else False
            if not(ingest_accepted): raise TrftTrainerException(f'We were unable to ingest your data at this point. {CONTACT_SUPPORT}')
            await progress_stage_II

            # Start Training
            trigger_id        = self._find_trigger_in_synced_config()[0]['id']
            workshop_id       = self._find_trained_models_workshop_in_synced_config()['id']
            training_settings = self._find_trainer_settings_in_synced_config(training_run_id)
            # tracks status updates sent from the API and displays them to the user
            progress_stage_III = asyncio.create_task(
                self.display_progress_stage_III(trigger_id, training_run_id)
            )
            training_trigger_params = {'triggerID': trigger_id, 'workshopModuleID': workshop_id, 'settings': training_settings}
            start_training_task = asyncio.create_task(trigger_pipeline(training_trigger_params, tofu_gql))
            await start_training_task
            maybe_training_task_started = start_training_task.result()
            training_accepted = maybe_training_task_started['triggerPipeline'] if 'triggerPipeline' in maybe_training_task_started else False
            if not(training_accepted): raise TrftTrainerException(f'We were unable to start your training at this point. {CONTACT_SUPPORT}')
            await progress_stage_III

            # reset display
            self.display_p = None

            # init trained model and return
            if return_trained_model: return TrftModel.load(trained_models_do['id'], training_id=training_run_id) 
