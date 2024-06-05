
class PartitionConfig:
    """
    Creates a structured schema for a subpartition training.

    Args:
        group_defining_columns (list):                Names of the columns that define a group member
        train_data_defining_columns (list[dict]):     Schema of the data columns to train on (that are not user defining). This can be question/ reply pairs where column name is the question and col. value is the reply.
        partition_at (dict):                          A parameter (existing column) that splits the groups. Must be a value of group_defining_columns
        unique_id_column (string):                    A parameter (existing column) that holds a unique value for each row (e.g. an ID)



    Examples:

        >>> # Defines the group (e.g. demographically split users)
        >>> group_defining_columns = ['name', 'gender', 'monthly_income']

        >>> # Defines the training data schema
        >>> train_data_defining_columns = [{
        >>>     'columName':  'how much do you  spend on skincare products monthly',
        >>>     'dataType': 'string',
        >>>     'valueType': 'enum',
        >>>     'validOptions': ['option a', 'option b', 'option c']
        >>>     },{
        >>>     'columnName': 'where do you shop for skincare products?',
        >>>     'dataType': 'string',
        >>>     'valueType': 'multipleChoice',
        >>>     'validOptions': ['Brand websites', 'Department stores', 'option c']
        >>>     },
        >>>    {
        >>>     'columnName': 'tell me something about yourself',
        >>>     'dataType': 'string',
        >>>     'valueType': 'freeText',
        >>>     },
        >>> ]

        >>> # Divide data into groups
        >>> partition_at = {
        >>>     'column': 'monthly_income',
        >>>     'dataType': 'int',
        >>>     'groups': [{
        >>>         'name': 'low_spenders',
        >>>         'lower_bound': 0,
        >>>         'upper_bound': 50,
        >>>     },{
        >>>         'name': 'mid_spenders',
        >>>         'lower_bound': 51,
        >>>         'upper_bound': 150,
        >>>     },{
        >>>         'name': 'high_spenders',
        >>>         'lower_bound': 151,
        >>>         'upper_bound': inf,
        >>>     }]
        >>> }

        >>> ### Groups can be partitioned with a lower and upper bound (see above). However when working with string data that cannot be directly compared, we need to define all options in a group:
        >>> partition_at = {
        >>>     'column': 'monthly_income',
        >>>     'dataType': 'string',
        >>>     'groups': [{
        >>>         'name': 'low_spenders',
        >>>         'members': ['<5€', '5€-25€', '26€ - 50€'],
        >>>     },{
        >>>         'name': 'mid_spenders',
        >>>         'members': ['51€ - 100€', '100€ - 150€'],
        >>>     },{
        >>>         'name': 'high_spenders',
        >>>         'members': ['above 150€'],
        >>>     }]
        >>> }

    Important:
        `userDefiningcolumns` and `partition_at` depend on each other.The `partition_at` column must be present inside `userDefiningcolumns` and the definition in `groups` must represent the data passed to the trainer.

    """
    # TODO check partition_at keyis in group_defining_columns
    def __init__(self, group_defining_columns, train_data_defining_columns, partition_at, unique_id_column):
        self.group            = group_defining_columns
        self.train            = train_data_defining_columns
        self.splitpoint       = partition_at
        self.unique_id_column =  unique_id_column

class Subspace:
    """
    Divides multiple sub groups into partions of the trained layer 


    Args:
        partition_config (transforms.autobrew.trft.Subspace.PartitionConfig): A config representing the subspace partitioning scheme
        rank (int): The rank of the trained layer.
    """
    def __init__(self, config: PartitionConfig, rank: int=8, via_ranges=False, via_explicit=True):
        self.config = config
        self.partitions = self.create_subspace_partition(via_ranges=via_ranges, via_explicit=via_explicit)

    def create_subspace_partition(self, via_ranges=False, via_explicit=False)->list:
        """
        Creates a subspace partition list targeting layers
        Either defines the layers as layer partition ranges `[[0, 384], [384, 768]]` or explicitly names the partitions `[[[0,1,3,4]]]`

        Arguments:
            via_ranges (bool): Wether or not defining via a range (s. above)
            via_explicit (bool): Wether or not defining partitions explicitly (s. above)

        Note:
            Either `via_ranges` or `via_explicit` need to be `True`
        """
        assert via_ranges or via_explicit, 'either `via_ranges` or `via_explicit` must be `True`'

        # TODO: should return named subspaces 
        if via_explicit: return list(list(range(len(self.config.splitpoint['groups']) * 4)))

        raise Exception('via_ranges is not implemented')

    # helper
    def _build_dict(self, seq, key):
        return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

    def get_partition(self, column_name, key='name', groups='groups'):
        """
        Returns the elements for this named partition

        Example:
            >>> subspace.get_partition('low_spenders')
            >>> #[0,1,2,3]
        """
        # get the partitions e.g. [0,1,3,4]
        partition_list = self.config.splitpoint[groups]
        # get the list indexable
        subspace_by_name = self._build_dict(partition_list, key=key)
        assert column_name in subspace_by_name, f'Expected {column_name} to be a valid partition your subspace. Likeley the partition has not been part of the training.'
        # get the index
        partition_index = subspace_by_name[column_name]['index'] * 4
        # return the block that represents this named partition
        return self.partitions[partition_index : partition_index + 4]


    def mix_subspaces(self):
        """
        Returns the groups as subspaces with a single boundary dimension
        """
        # for each group count 3 entries, leave one boundary entry empty e.g. len(groups) = 1 ==> [0,1,2,3], len(groups)=2 => [0,1,2,3, 5,6,7]
        enumerated_splits = [index for index, _ in enumerate(self.config.splitpoint['groups'])]
        boundary_mixed_spaces = [i for item in enumerated_splits for i in range(item * 4 + 1, (item + 1) * 4 + 1) if i % 4 != 0]
        return [[boundary_mixed_spaces]]

