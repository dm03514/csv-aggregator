import ConfigParser
import csv
import glob
import os
import sys


class CSVAggregator(object):

    def __init__(self, 
                 config_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'columns.cfg')):
        """
        Initialize new CSV aggregator. config_path is the full
        path to the config file, it defaults to the main project
        dir, this will assign the config options to variables
        to be used later.
        """
        # make sure to get config options
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        self.rules = self._parse_config_options(config) 
        self.output_columns_list = config.options('output_columns')
        # initialize output file
        self.output_f = open('output.csv', 'wb')


    def aggregate_csv(self, csv_path):
        """
        Read a csv and transform it according to aggregation rules
        Use DictReader to get field names
        @return void writes to output file
        """
        # open this csv
        with open(csv_path) as f:
            # run through csv reader
            dict_reader = csv.DictReader(f.read())



    def _parse_config_options(self, config, section='rules'):
        """
        Helper function to populate config options dict
        @return dict {'column_from': 'column_to'}
        """
        output = {}
        options = config.options(section) 
        for option_key in options: 
            output[option_key] = config.get(section, option_key)
        return output 



if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        raise Exception('Please include a valid path')
    aggregator = CSVAggregator()
    for csv_path in glob.glob('{0}/*.csv'.format(sys.argv[1])):
        # make sure that this isn't the output csv.
        # where should the output csv be? I'd like to put it
        # in memory but these csvs can be HUGGGGE
        if 'output.csv' in csv_path:
            continue
        csvs_list = aggregator.aggregate_csv(csv_path)
