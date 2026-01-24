from read_data import read_csv
import argparse

def load_save_data(parameters_yaml_path: str):

    # Load data using read_csv function
    df = read_csv(parameters_yaml_path = parameters_yaml_path)
    print("Data loaded successfully")

    # There are spaces between column names, removing them.
    # For example: 'fixed acidity, 'volitile acidity' -> 'fixed_acidity', 'volitile_acidity'
    df.columns = [col.replace(" ", "_") for col in df.columns]
    print("Columns renamed successfully")

    # Save the dataset to data/raw
    raw_data_path = r"data/raw/raw_winequality.csv"
    df.to_csv(raw_data_path, index = False)

    print(f"Data saved to {raw_data_path} successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameters_yaml_path", default="parameters.yaml")
    args = parser.parse_args()
    load_save_data(parameters_yaml_path = args.parameters_yaml_path)
