# Read parameters.yaml   (To get the path of original csv file)
# Read original csv file
# Return a dataframe

import yaml
import pandas as pd
import argparse

# Defining a function to read yaml file, get csv file path and read csv file

def read_data(parameters_path: str)-> pd.DataFrame:

    # Read parameters.yaml file
    with open(parameters_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
    
    csv_file_path = data['data_source']['local_data_path']

    # Read csv file
    df = pd.read_csv(csv_file_path)

    return df



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--parameters_path", default = "parameters.yaml")
    parsed_args = args.parse_args()
    data = read_data(parameters_path = parsed_args.parameters_path)
    print(data.head())