import ConfigParser
import csv
from datetime import datetime
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
        config.optionxform = str
        config.read(config_path)
        self.rules = self._parse_config_options(config) 
        self.output_columns_list = config.options('output_columns')
        # initialize output file as a dict writer
        output_file_name = datetime.now().strftime('output_%Y_%m_%d_%H_%M_%S.csv')
        #import ipdb; ipdb.set_trace()
        f = open(output_file_name, 'wb')
        self.dict_writer = csv.DictWriter(f, self.output_columns_list)
        # write output columns
        self.dict_writer.writeheader()

    def aggregate_csv(self, csv_path):
        """
        Read a csv and transform it according to aggregation rules
        Use DictReader to get field names
        @return void writes to output file
        """
        # open this csv
        with open(csv_path) as f:
            # run through csv DictReader to get field names
            dict_reader = csv.DictReader(f)
            # for every row check if it is in the output columns or if it
            # is in one of the mappings (case sensitive)
            for line_dict in dict_reader:
                new_row_dict = {}
                # apply rules
                line_dict = self._apply_rules(self.rules, line_dict)  

                # go through output columns and compose a row to write
                for column_name in self.output_columns_list:
                    try:
                        new_row_dict[column_name] = line_dict[column_name]
                    except KeyError:
                        pass

                self.dict_writer.writerow(new_row_dict)

    def _apply_rules(self, rules, line_dict):
        """
        Apply all rules to a line dict.  This consists of converting any
        columns specificed in rules to the output column
        @return dict the modified dict with rules applied.
        """
        for from_name, to_name in rules.items():
            if from_name in line_dict:
                # rename this key
                line_dict[to_name] = line_dict[from_name]
                del line_dict[from_name]

        return line_dict            

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
