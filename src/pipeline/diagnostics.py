"""
This file is responsible for the execution of diagnostics 
in the model and in the system process.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import pickle
import subprocess
import pandas as pd
import logging as log
import timeit
import os
import json

from src.pipeline.pipeline import Pipeline
from src.utils.projects_paths import BASE_PATH, CONFIG_FILE


class DiagnosticsPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.dataset_csv_path = os.path.join(
            BASE_PATH, config['output_folder_path'])
        self.test_data_path = os.path.join(BASE_PATH, config['test_data_path'])
        self.model_path = os.path.join(
            BASE_PATH, config['prod_deployment_path'], 'trainedmodel.pkl')
        self.metrics_path = os.path.join(
            BASE_PATH, config['output_metrics_path'])

    def model_predictions(self):
        """Read the deployed model and a test dataset, 
            calculate predictions

        Returns:
            list: Returns a list containing all predictions
        """
        data = pd.read_csv(os.path.join(self.test_data_path, 'testdata.csv'))
        y = data['exited']
        X = data.drop(['corporation', 'exited'], axis=1)

        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)

        y_pred = model.predict(X)

        return y_pred.tolist()

    def dataframe_summary(self):
        """Calculate summary statistics

        Returns:
            list: Returns a list containing all summary statistics
        """
        df = pd.read_csv(os.path.join(self.dataset_csv_path, 'finaldata.csv'))
        df = df.drop(['corporation', 'exited'], axis=1)

        stats_dict = {}
        stats_dict['col_means'] = dict(df.mean())
        stats_dict['col_medians'] = dict(df.median())
        stats_dict['col_std'] = dict(df.std())

        return stats_dict

    def execution_time(self):
        """Calculate timing of training.py 
            and ingestion.py

        Returns:
            list: Returns a list of 2 timing values in seconds
        """
        times = []
        for file in ['ingestion','training']:
            starttime=timeit.default_timer()
            _ = subprocess.run(['python', 'main.py', '-p', file])
            timing = timeit.default_timer()-starttime
            times.append(timing)
        return times

    def outdated_packages_list(self):
        """Function to check dependencies

        Returns:
            list: Returns the list of outdated dependencies
        """
        outdated = subprocess.run(
            ['pip', 'list', '--outdated', '--format', 'json'], capture_output=True).stdout
        outdated = outdated.decode('utf8').replace("'", '"')
        outdated_list = json.loads(outdated)
        return outdated_list

    def missing_data(self):
        """This functions is to check the percentage of 
           missing data in the finaldata file.

        Returns:
            list: Returns the list containing the percent of NAs
        """        
        data = pd.read_csv(os.path.join(self.dataset_csv_path, 'finaldata.csv'))
        percent_na = list(data.isna().sum(axis=1)/data.shape[0])
        return percent_na

    def run(self):

        list_of_predictions = self.model_predictions()
        stats_dict = self.dataframe_summary()
        list_of_times = self.execution_time()
        outdated_list = self.outdated_packages_list()
        percent_na = self.missing_data()

        diagnostics = {
            "TestDataPrediction": list_of_predictions,
            "DataFrameSummary": stats_dict,
            "ExecutionTimes": list_of_times,
            "PackagesOutdated": outdated_list,
            "MissingData": percent_na
        }

        log.info(f"Savind Diagnostics in {self.metrics_path}")
        with open(os.path.join(self.metrics_path, 'diagnostics.json'), 'w') as file:
            file.write(json.dumps(diagnostics))
