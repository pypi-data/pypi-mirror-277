import asyncio
import json
import os
import pprint
from uuid import uuid4
from pandas import DataFrame

from ohmytofu.autobrew.trft.resolvers import batch_ingest, trigger_pipeline, object_view
from ohmytofu.connectivity.sse import handle_sse_events, listen_to_sse_stream
from ohmytofu.log import EvalConfig, EvalStats, EvalResults, EvalMetric
from ohmytofu.autobrew.trft.Subspace import PartitionConfig, Subspace
from ohmytofu.display._display import TaskProfile
from ohmytofu.display import display
from datetime import datetime
from uuid import uuid4

from ohmytofu.model._model import (
    ModelOutput,
    ModelUsage
)
import time

from ohmytofu.utils.runtime import block
from ohmytofu.connectivity.gql.queries import (
    list_models_query,
    model_config_query,
)

class NoDatasetException(Exception):
    pass

class SamplerInvalidConfigException(Exception):
    pass

class EnvironmentException(Exception):
    pass

API_BASE = 'https://db.tc.ohmytofu.ai'
READABLE_VALUETYPES = {
    'multipleChoice': 'Multiple Choice',
    'enum': 'Single Choice',
    'freeForm': 'Free Form Text'
}



def list_models():
    """
    Lists TrftModels available to load via the TrftModel class.
    """
    from ohmytofu.connectivity.gqlclient import client as tofu_gql
    res = _list_models(client=tofu_gql)
    if 'dataObjectTypes' not in res: raise Exception("could not find any models in your account. Contact support@ohmytofu.ai if you have any questions.")
    return res['dataObjectTypes']

@block
async def _list_models(client, api_class='trainedModels'):
    """
    Executes a list model query.
    """
    # selector for the api class
    where = {"where": {"apiName": api_class}}
    return await client.execute_async(list_models_query, variable_values=where)

async def _get_model_config(model_id_or_path, training_id=None, client=None):
    if client is None: from ohmytofu.connectivity.gqlclient import client
    variables = {"id": model_id_or_path, "trainingID": training_id}
    config_request = await client.execute_async(model_config_query, variable_values=variables)
    if 'getTrftModelConfig' not in config_request: raise Exception('could not find config')
    return config_request['getTrftModelConfig']


class TrftSampler():
    def __init__(self, question="How is your day?", value_type="freeForm", data_type="string", valid_options=[]):
        # sanity check config # TODO: make pydantic dataclass
        if READABLE_VALUETYPES.get(value_type, None) is None:
            raise SamplerInvalidConfigException(f'The value type you provided is invalid. Please chose from {READABLE_VALUETYPES.keys()}')

        self.question = question
        self.value_type = value_type
        self.data_type  = data_type
        self.valid_options = valid_options

    def to_dict(self):
        return {
         'columnName': self.question,
         'dataType': self.data_type,
         'valueType': self.value_type,
         'validOptions': self.valid_options,
        } 

class TrftModel:
    """
    Loads a trained Trft (Tofu Raft) Model. Assumes the model has been trained with TrftTrainer.

    Example:
        >>> from ohmytofu.autobrew.trft.model import TrftModel
        >>> # load the model. When unsure about the training_id, a list of training_id's will be printed when omitting the parameter.
        >>> trft = TrftModel.load('model-name-or-id', training_id="some-id-returned-from-train-run") 
        >>> # generate a result from your prompt
        >>> res = trft.model.generate(trft.model.tokenizer('....', return_tensors='pt').to(tft.device))
        >>> # decode the result
        >>> generated_text = trft.tokenizer.decode(res[1][0])
    """
    def __init__(self, rid, preloaded_config=None, base_model_only=False, device='cuda', training_id=None, debug_level=0):
        from ohmytofu.connectivity.gqlclient import client as tofu_gql
        self.model_path = rid # not loaded any model so far
        self.model = None
        self.base_model = None # TODO: experimental
        self.base_model_config = None
        self.base_model_name_or_path = None
        self.tokenizer = None
        self.device = device
        self.pretrained_config = None
        self.base_model_config = None
        self.subspace = None
        self.client = tofu_gql
        self.preloaded_config = preloaded_config
        self.raw_dataset = None
        self.rid = rid
        self.training_id = training_id
        self.display_p = None

        if not base_model_only:
            # get the base model name and config from it's config file
            #pretrained_config,_ = PretrainedConfig.get_config_dict(f'{self.model_path}/{base_model_config_path}')
            self.base_model_config = preloaded_config['baseConfig']
            self.base_model_name_or_path = self.base_model_config['_name_or_path'] 
            # init the subspace
            self.subspace = self.load_subspace() # assumes save_configs are 'group', 'train', 'splitpoint

        # when loading base model only
        if self.base_model_name_or_path is None: self.base_model_name_or_path = model_path

    async def get_model_config(self, model_id_or_path, training_id=None):
        return await _get_model_config(model_id_or_path, training_id=training_id, client=self.client)


    def _handle_status_message(self, message, td, finish_prev_task=False, prev_task=None, total_steps=20, debug_level=0):
        # finish the previous task
        if finish_prev_task and prev_task: self._progress(
                prev_task['p'],
                name=prev_task['name'],
                n=prev_task['total_steps']+1
        )

        has_progress = 'progress' in message and 'total' in message
        is_update = 'isUpdate' in message and message['isUpdate'] == True
        step = None
        if has_progress: step = message['progress']
        else: print(f"noprogress msg: {message}")
        #  print('handling message')
        #  print(message)
        if is_update: return self._progress(self.display_p, n=step if has_progress else None, name=message['status'])
        with td.progress(total=message['total'] if has_progress else None) as self.display_p:
            self._progress(self.display_p, n=step if has_progress else None, name=message['status'])
        #name = "Running Model"
        #jtime.sleep(2.0)
        #for i in range(5):
        #    time.sleep(1)
        #    self._progress(p, n=50, name=name)
        
    #  with td.progress(total=total_steps) as p:
#
#
        #  progress(name="Getting summarizer")
        #  time.sleep(2.0)
#
        #  name = "Running summarizer"
        #  time.sleep(2.0)
        #  for i in range(5):
            #  time.sleep(1)
            #  progress(n=50, name=name)
#
    #  with td.progress(total=100) as p:
#
        #  name = "Writing data"
        #  progress(name=name)
        #  time.sleep(2.0)
        #  for i in range(3):
            #  time.sleep(1)
            #  progress(n=150, name=name)


    def _progress(self, p, n=0, name="Task") -> None:
        p.update(n, name=name)

    async def display_progress(self, batch_trigger_id, batch_id, show_summary=True):
        def now ():
            return datetime.now().isoformat()

        # TODO
        eval_cfg = EvalConfig(
            epochs=1
        )
        # TODO
        profile = TaskProfile(
            name="Simulatrex Pipeline",
            batch_id=batch_id,
            sequence=[0,1],
            model="TofuAI",
            dataset="testDS",
            scorer="(none)",
            samples=200,
            eval_config=eval_cfg,
            log_location=None,
            task_args={},
            generate_config=None
        )
        start_timer = now()
        # TODO 
        total_steps = 20 

        with display().task(profile) as td:

            with td.progress(total=total_steps) as p:
                # initial task display
                task_name = 'Acquiring GPU'
                self._progress(p, name=task_name)

                # setup a status message listener with callback
                this_task = {'p': p, 'total_steps': total_steps, 'name': task_name}
                # callback
                on_msg_callback  = lambda msg: self._handle_status_message(
                    msg,
                    td=td,
                    prev_task=this_task,
                    finish_prev_task=True
                )
                task_events = asyncio.create_task(
                    listen_to_sse_stream(
                        batch_trigger_id, 
                        tofu_type="triggerPipeline",
                        on_message=on_msg_callback,
                    )
                )

            # wait for status updates
            await task_events
            print('DONE')
            return
            # TODO show_summary


            """    
            eval_results = EvalResults(
                metrics={'Evaluation Score': EvalMetric(name="Eval", value=0.1)}
            )
            eval_results = EvalResults(metrics={})
            model_usage = ModelUsage(input_tokens=120, output_tokens=42, total_tokens=162)
            eval_stats = EvalStats(
                started_at=start_timer,
                completed_at=now(),
                )


            td.summary(
                eval_results,
                eval_stats,
                batch_id,
                )
            """



    @block
    async def batch_generate(
            self,
            sampler,
            template,
            dataset=None,
            partition_name=None,
            max_new_tokens=128,
            temperature=0.4,
            cleanup=True,
            device='cuda',
            batch_size=32,
            batch_debug=False,
            mix_subspaces=False,
            model_rid_or_path=None,
            construct_prompts_from_dataset=False,
            return_type='pandas',
            debug_level=0,
    ):
        """
        Convenience function to generate text with the model on a subpartition with batches of text (more efficient).

        Example:
            >>> from ohmytofu.autobrew.trft.model import TrftModel
            >>> # load the model
            >>> trft = TrftModel.load('model-name-or-id')
            >>> # generate a result from your prompt
            >>> res = trft.batch_generate( 
            >>>     prompts=[instruction]*1024, # 1024 repetiotions of the same prompt
            >>>     template='%s',
            >>>     partition_name='mid_spenders',
            >>>     temperature=0.1,
            >>>     cleanup=True
            >>> )
            >>> len(res) # 1024 results
            >>> 

            Instead of a fixed partition name, one can also mix the subspaces

            >>> res = trft.batch_generate( 
            >>>     prompts=[instruction]*1024, # 1024 prompts
            >>>     template='%s',
            >>>     partition_name=None,
            >>>     mix_subspaces=True, # mixes the trained subspaces equally
            >>>     temperature=0.1,
            >>>     cleanup=True
            >>> )
            >>> len(res) # 1024 results
            >>> 
        """

        from ohmytofu.connectivity.gqlclient import client as tofu_gql
        assert isinstance(sampler, TrftSampler), 'Please use a TrftSampler configured for your question and its answer and data types'
        assert isinstance(dataset, DataFrame), 'Please use a pandas dataframe as the dataset'

        status_messages = []
        self.raw_dataset = dataset
        batch_dataset =  self.build_dataset(
            dataset_output_type='pandas',
            drop_output=False,
            select_group=partition_name,
            sampler=sampler
        )

        batch_id = str(uuid4())
        batch_trigger_ID = self.preloaded_config['triggerConfig']['id']

        if 'TOFU_WORKSHOP_ID' not in os.environ: raise EnvironmentException('could not find your `TOFU_WORKSHOP_ID` configured in your environment. We can help you at support@ohmytofu.ai at any point of your project.')
        workshop_id = os.environ['TOFU_WORKSHOP_ID']

        batch_prompts_do   = self.preloaded_config['dataObjects']['batchPrompts']
        trained_models_do  = self.preloaded_config['dataObjects']['trainedModels']
        generated_texts_do = self.preloaded_config['dataObjects']['generatedTexts']

        trained_models_id  = trained_models_do['id']
        batch_prompts_id   = batch_prompts_do['id']
        batch_prompts_rid  = batch_prompts_do['rid']
        generated_text_rid = generated_texts_do['rid']

        data = [{
            "id": str(uuid4()),
            "batch_id": batch_id,
            "interview_question": sample['instruction'],
            "generated": "False",
            "generated_text": "None",
        } for sample in batch_dataset.to_records()]
        n_replies = len(data)

        batch_ingest_params = {
            "rid": batch_prompts_rid.replace('_', '.'), # we're migrating away from the `_` syntax
            "primaryKey": "id",
            "data": data,
        }

        # TODO
        # tracks status updates sent from the API and displays them to the user
        listen_for_updates_and_display_task = asyncio.create_task(self.display_progress(batch_trigger_ID, batch_id))
        _ingest_task_event = asyncio.create_task(handle_sse_events(batch_prompts_rid.replace('.', '_'), tofu_type="dataObjectType"))
        # ingest the data
        batch_ingest_task = asyncio.create_task(batch_ingest(batch_ingest_params, tofu_gql))
        await batch_ingest_task
        ingest_result = batch_ingest_task.result()

        # this has only started the ingest, we are waiting to complete the sse task
        maybe_started_ingest = ingest_result['batchIngestData']
        if not maybe_started_ingest:
            raise Exception('did not start ingest successfully')

        # wait for the data ingest to complete
        await _ingest_task_event
        # value separator
        answerOptionSeparator = '<|SEP|>'

        ## construct datafields as the input to the pipeline
        datafields = [
            {
            'name': '**output_rid', ## where to write generated data to
            'value': generated_text_rid
            },
            {
            'name': '**overwrite',    ## feature flag that confirms an overwrite, this is needed since there's no data yet that could be appended to
            'value': 'false' ## send as string
            },
            {
            'name': 'batch_id', ## selects the batch
            'value': batch_id
            },
            {
            'name': 'training_id', ## selects the model
            'value': self.training_id
            },
            {
            'name': 'interview_question', ## this is the question that leads to the final answer, e.g. `What is your most urging skin concern?`
            'value': sampler.question
            },
            {
            'name': 'answer_options', ## this is the question that leads to the final answer, e.g. `What is your most urging skin concern?`
            'value': answerOptionSeparator.join(sampler.valid_options)
            },
            {
            'name': 'answer_options_type', ## this is the question that leads to the final answer, e.g. `What is your most urging skin concern?`
            'value': sampler.value_type
            },
            {
            'name': 'answer_options_separator', ## used in the pipeline to revert the join operation and make the string a list again
            'value': answerOptionSeparator
            },
            {
            'name': 'trained_models_id', ## takes part in selectigg the model
            'value': trained_models_id
            },
            {
            'name': 'batch_dataset_id',
            'value': batch_prompts_id
            },
            {
            'name': 'apiBase',
            'value': API_BASE
            },
            {
            'name': 'apiKey',
            'value': os.environ['TOFU_API_KEY']
            },
            {
            'name': '**batch_trigger_id', # gives us an sse_logger in the pipeline
            'value': batch_trigger_ID
            }
        ]

        trigger_variables = {'triggerID': batch_trigger_ID, 'workshopModuleID': workshop_id}
        trigger_variables_with_settings = {**trigger_variables, 'settings': {'datafields': datafields}}

        # trigger the pipeline
        _batch_generate_event = asyncio.create_task(handle_sse_events(generated_text_rid, tofu_type="dataObjectType"))

        batch_generate_task = asyncio.create_task(trigger_pipeline(trigger_variables_with_settings, tofu_gql))
        await batch_generate_task
        # wait for it to complete
        await _batch_generate_event
        # pull generated data
        object_view_params = {
            "rid": generated_text_rid,
            "primaryKey": "id", 
            "filterSecondaryKey": "batch_id",
            "value": batch_id
        }
        data_sync_task = asyncio.create_task(object_view(object_view_params, tofu_gql))
        await data_sync_task
        synced_data = data_sync_task.result()
        # return as json or pandas Dataframe
        if return_type == 'json': return synced_data
        return DataFrame.from_records(synced_data)

    def split_dataset_partition(self, dataset, group_name_key='name'):
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
        
        print(f""" 
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

    # helper
    def _build_dict(self, seq, key):
        return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))


    def _get_config_kv(self, seq, key='validOptions', col_identifier='columnName'):
        # filter invalid entries
        valid_seq = [d for d in seq if key in d]
        return dict((d[col_identifier], d[key]) for (index, d) in enumerate(valid_seq))

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


    def _postprocess_ds(self, ds, sampler=None):
        """
        Builds a instruction dynamically with the provided subspace schema.
        """
        # build the template
        template = """{group_def_template}\n{question}. ({value_type}, Options: {options}):""" 

        # get dicts of question answer pairs
        group_def_data = [{item: ds[item]} for item in self.subspace.config.group]
        # join them to a string
        group_def_template = '\n'.join([f"{key}: {value}" for d in group_def_data for key, value in d.items()])

        seq = self.subspace.config.train if sampler is None else [sampler.to_dict()]
        # read the value type and translate it to a human readable form
        value_type_cfg = self._get_config_kv(
            seq=seq,
            key='valueType'
        )[ds['question']]
        # get the human readable form, if not possible just pass on what was in the config
        value_type = READABLE_VALUETYPES.get(value_type_cfg, value_type_cfg)

        # get valid options
        options = self._get_config_kv(
            seq=seq,
            key='validOptions'
        )[ds['question']] if value_type_cfg in ['multipleChoice', 'enum'] else None

        options_text = ', '.join(options) if options else ''

        # format the instruction
        instruction = template.format(
            question=ds['question'],
            options=options_text,
            value_type=value_type,
            group_def_template=group_def_template,
        )
        # TODO: clean options strings on freeform
        
        return instruction

    def build_dataset(self, dataset=None, dataset_output_type='dataset', drop_output=True, select_group=None, sampler=None):
        from pandas import concat, melt
        from datasets import Dataset

        if self.raw_dataset is None and dataset is not(None):
            self.raw_dataset = dataset
        
        if self.raw_dataset is None and dataset is None: raise NoDatasetException('no dataset supplied')

        # read splitpoint data and make a split dataset by partition
        ds_partitioned = self.split_dataset_partition(self.raw_dataset)

        # filter for grups if given
        subset = None
        if select_group:
            subset = next((group for group in ds_partitioned if group['name'] == select_group), None)
            ds_partitioned_subset = [subset]
        # preprocess dataset to add subpartition for data collator
        ds_preprocessed = self.preprocess_dataset_for_raft(ds_partitioned if subset is None else ds_partitioned_subset) 
        # combine back to one dataset, the partitions are now expressed in the `subpartition` column
        subspace_dataset = concat([partitioned_dataset['dataset'] for partitioned_dataset in ds_preprocessed])
        # collect columns we want to have in every row of the training dataset
        keep = [col for col in self.subspace.config.group] + ['subspaces']
        df_interest = subspace_dataset[keep]

        # keep these in every row
        cols_for_every_row = self.subspace.config.group + ['subspaces']

        if sampler:
            df_prompt = df_interest.copy()
            df_prompt.loc[:,'question'] = sampler.question
        else:
            # melt into simple questions
            # turn the multi column dataset into multiple rows, one for each question while keeping the columns defined in `keep`
            df_prompt = melt(df_interest, id_vars=cols_for_every_row, var_name="question", value_name="output", ignore_index=True) 

        # make an instruction from template and questio by applying the template
        #  instruction_ds =
        df_prompt.loc[:,'instruction'] = df_prompt.apply(lambda ds: self._postprocess_ds(ds, sampler=sampler), axis=1)
        # our trainer is using the Alpaca dataset format which has an input field, it can be empty though
        #df_prompt['input'] = ''

        if drop_output:
            df_prompt = df_prompt.drop('output', axis=1)

        if dataset_output_type == 'pandas': return df_prompt

        return Dataset.from_pandas(df_prompt)

    def preprocess_dataset_for_trft(self, dataset, partitioned=True):
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

    def load_subspace(self, save_configs=['groupConfig', 'trainConfig', 'splitpointConfig']):
        loaded_cfg = {}
        # load subspace defining config from model path
        for config_name in save_configs:
            config = self.preloaded_config[config_name]
            loaded_cfg.update({config_name: config})

        # get the keys defining the settings
        group_key = save_configs[0]
        train_key = save_configs[1]
        parti_key = save_configs[2]

        # create partition config from loaded data
        pc = PartitionConfig(
            group_defining_columns=loaded_cfg[group_key],
            train_data_defining_columns=loaded_cfg[train_key],
            partition_at=loaded_cfg[parti_key]
        )

        # return the subspace for the data
        return Subspace(pc)

    @classmethod
    @block
    async def load(
        cls,
        model_id_or_path,
        device='cuda',
        base_model_config_path='base_config.json',
        use_fast_tokenizer=False,
        training_id=None
    ):
        """
        Load a trained model.

        Arguments:
        model_id_or_path (str): Name or ID of a trained TrftModel. Get a list of models with `list_models()`
        device     (str): Either `cuda` (GPU) or `cpu`
        base_model_config_path (str): The filename inside the `model_path` defining the configuration of the base model
        use_fast_tokenizer (bool): Wether to use the `tokenizer_fast` of the model
        training_id (str): ID of the training run
        """
        raw_config = await _get_model_config(model_id_or_path, training_id=training_id)
        model_path = raw_config['modelPath']
        initialized_cls = cls(model_path, preloaded_config=raw_config, device=device, base_model_only=False, training_id=training_id)
        return initialized_cls
