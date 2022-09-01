"""
This file is responsible for scoring the trained model.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import pandas as pd
import pickle
import os
import logging as log
from sklearn import metrics
import json

from src.utils.projects_paths import BASE_PATH, CONFIG_FILE


class Scoring:

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.dataset_csv_path = os.path.join(
            BASE_PATH, config['output_folder_path'])
        self.model_path = os.path.join(BASE_PATH, config['output_model_path'])
        self.metrics_path = os.path.join(
            BASE_PATH, config['output_metrics_path'])
        self.test_data_path = os.path.join(BASE_PATH, config['test_data_path'])

    def score_model(self, data_path: str = None):
        """This function should take a trained model, load test data, 
            and calculate an F1 score for the model relative to the 
            test data it should write the result to the latestscore.txt

            Returns:
            double: F1 Score for the model on the data.
        """
        if data_path == None:
            test_df = pd.read_csv(os.path.join(self.test_data_path, 'testdata.csv'))
        else:
            test_df = pd.read_csv(os.path.join(BASE_PATH, data_path))

        X_test = test_df.drop(['corporation', 'exited'], axis=1)
        y_test = test_df['exited']

        with open(os.path.join(self.model_path, 'trainedmodel.pkl'), 'rb') as file:
            model = pickle.load(file)

        y_pred = model.predict(X_test)
        f1_score = metrics.f1_score(y_test.values, y_pred)
        log.info(f'F1 Score: {f1_score}')

        log.info(f"Savind F1 score in {self.metrics_path}")
        with open(os.path.join(self.metrics_path, 'latestscore.txt'), 'w') as file:
            file.write(str(f1_score))
        return f1_score
