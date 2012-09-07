csv-aggregator
==============

A tool for combining csvs with possible different column names.  It is easy to create rules to change column names and
merge data from multiple csvs.

***

## Usage:

The columns.cfg file is the core of this utility.  It has 2 sections, [rules] and [output_columns]

Output columns are all the columns the output csv should contain.  Since config parser entries take the form of `key: value` all config items must contain `output_column_name: true`

The [rules] section contains mappings of column names,  THese are applied to each row of the csv files.


`python csv_aggregator.py <path/to/csv/input/files>`

The above command will read from the columns.cfg file and create an output.csv file in the current directory!


    usage: csv_aggregator.py [-h] [-c CONFIG_PATH] [-o OUTPUT_PATH] csv_path

    Aggregate CSV files based on config file

    positional arguments:
      csv_path              path where csvs to aggregate are located

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_PATH, --config CONFIG_PATH
                            path to config file
      -o OUTPUT_PATH, --output OUTPUT_PATH
                            full path of output file
