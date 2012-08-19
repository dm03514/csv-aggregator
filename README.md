csv-aggregator
==============

A tool for combining csvs with possible different column names

***

## Usage:

The columns.cfg file is the core of this utility.  It has 2 sections, [rules] and [output_columns]

Output columns are all the columns the output csv should contain.  Since config parser entries take the form of `key: value` all config items must contain `output_column_name: true`

The [rules] section contains mappings of column names,  THese are applied to each row of the csv files.


`python csv_aggregator.py <path/to/csv/input/files>`

The above command will read from the columns.cfg file and create an output.csv file in the current directory!

