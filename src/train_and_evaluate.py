# ======================== Importing necessary modules ========================
from read_data import read_yaml
import pandas as pd
import numpy as np

# import ElasticNet model
from sklearn.linear_model import ElasticNet

# For metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# For model, parameters and metrics saving
import joblib
import json

import argparse


# ======================== Utility Functions ========================

def evaluate_model(actual, predicted):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)
    return rmse, mae, r2

# ======================== Final Workflow ========================



def train_and_evaluate_model(parameters_yaml_path: str):

    # Read parameters.yaml file
    yaml_data = read_yaml(parameters_yaml_path = parameters_yaml_path)
    print("YAML file successfully read")
    print("="*50)

    # Extracting file paths from yaml file
    train_data_path = yaml_data['split_data']['train_path']
    test_data_path = yaml_data['split_data']['test_path']
    models_path = yaml_data['models_path']

    # Extracting model parameters from yaml file
    alpha = yaml_data['algorithms']['ElasticNet']['parameters']['alpha']
    l1_ratio = yaml_data['algorithms']['ElasticNet']['parameters']['l1_ratio']
    random_state = yaml_data['base']['random_state']

    # Reading train and test data
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)

    print("Train and Test data successfully loaded")
    print("Train Dataframe shape:", train_df.shape)
    print("Test Dataframe shape:", test_df.shape)
    print("="*50)

    # Splitting data into X and y
    x_train = train_df.drop("target", axis = 'columns')
    y_train = train_df["target"]

    x_test = test_df.drop("target", axis = 'columns')
    y_test = test_df["target"]

    # Initializing ElasticNet model
    model_parameters = {
        "alpha": alpha,
        "l1_ratio": l1_ratio,
        "random_state": random_state}
    
    model = ElasticNet(**model_parameters)
    print("Model initialized with given parameters")
    print("="*50)

    # Training the model
    model.fit(x_train, y_train)
    print("Model training completed")
    print("="*50)

    # Making predictions
    y_pred = model.predict(x_test)
    print("Predictions on test data completed")
    print("="*50)

    # Evaluating the model
    rmse, mae, r2 = evaluate_model(y_test, y_pred)
    print(f"""Model Evaluation Metrics
          
          RMSE: {rmse}
          MAE: {mae}
          R2 Score: {r2}""")
    print("="*50)

    # ----------------------------------------------------------------------------------------------------

    # Saving the trained model, scores and parameters
    scores_file_path = yaml_data['reports']['model_scores_path']
    parameters_file_path = yaml_data['reports']['model_parameters_path']

    # Saving scores
    with open(scores_file_path, 'w') as f:
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2_score": r2
        }

        json.dump(scores, f, indent = 4)
    
    print("Model scores saved successfully")
    print()

    # Saving model parameters
    with open(parameters_file_path, 'w') as f:
        json.dump(model_parameters, f, indent = 4)
    print("Model parameters saved successfully")
    print("="*50)

    # Saving the trained model
    model_file_path = f"{models_path}/elasticnet_model.joblib"
    joblib.dump(model, model_file_path)

    print(f"Model saved to {model_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameters_yaml_path", default = 'params.yaml')

    args = parser.parse_args()

    train_and_evaluate_model(
        parameters_yaml_path = args.parameters_yaml_path
    )