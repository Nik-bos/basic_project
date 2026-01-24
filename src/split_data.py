from read_data import read_yaml
import argparse
import pandas as pd

# For splitting the data
from sklearn.model_selection import train_test_split

# =============================================

# Defining a function to split data into train and test and save them to respective paths
def split_and_save_data(parameters_yaml_path: str):

    # Read parameters.yaml file
    yaml_data = read_yaml(parameters_yaml_path = parameters_yaml_path)

    # Fetching required parameters from yaml data
    raw_data_path = yaml_data['load_data']['raw_dataset_path']
    train_data_path = yaml_data['split_data']['train_path']
    test_data_path = yaml_data['split_data']['test_path']
    test_size = yaml_data['split_data']['test_size']
    random_state = yaml_data['base']['random_state']

    # Read the raw dataset
    df_raw = pd.read_csv(raw_data_path)
    print("Raw data read successfully")
    print(f"Raw data shape-> {df_raw.shape}")

    # Splitting the data into train and test and saving them to respective paths
    train_data, test_data = train_test_split(
        df_raw,
        test_size = test_size,
        random_state = random_state
    )

    print("Data successfully split into train and test")
    print(f"Train data shape-> {train_data.shape}")
    print(f"Test data shape-> {test_data.shape}")

    # Saving the train and test data to respective paths
    train_data.to_csv(train_data_path, index = False)
    test_data.to_csv(test_data_path, index = False)

    print(f"Train data saved to {train_data_path} successfully")
    print(f"Test data saved to {test_data_path} successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameters_yaml_path", default = "parameters.yaml")
    args = parser.parse_args()

    # Calling the split_data function
    split_and_save_data(
        parameters_yaml_path = args.parameters_yaml_path
    )