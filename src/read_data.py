# Read parameters.yaml   (To get the path of original csv file)
# Read original csv file
# Return a dataframe

import yaml
import pandas as pd
import argparse

# Defining a function to read yaml file.
def read_yaml(parameters_yaml_path: str):
    with open(parameters_yaml_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data

# Defining a function to read yaml file, get csv file path and read csv file
def read_csv_file(parameters_yaml_path: str)-> pd.DataFrame:

    # Read parameters.yaml file
    yaml_data = read_yaml(parameters_yaml_path = parameters_yaml_path)

    csv_file_path = yaml_data['data_source']['local_data_path']

    # Read csv file
    df = pd.read_csv(csv_file_path)

    return df



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--parameters_yaml_path", default = "parameters.yaml")
    parsed_args = args.parse_args()
    data = read_csv_file(parameters_yaml_path = parsed_args.parameters_yaml_path)
    print(data.head())