
"""
This file is responsible for the execution of diagnostics 
in the model and in the system process.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import pickle
import pandas as pd
import numpy as np
import timeit
import os
import json

from src.pipeline.pipeline import Pipeline
from src.utils.projects_paths import BASE_PATH, CONFIG_FILE

class DiagnosticsPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE,'r') as f:
            config = json.load(f) 

        self.dataset_csv_path = os.path.join(BASE_PATH, config['output_folder_path']) 
        self.test_data_path = os.path.join(BASE_PATH, config['test_data_path']) 
        self.model_path =  os.path.join(BASE_PATH, config['prod_deployment_path'], 'trainedmodel.pkl') 

    ##################Function to get model predictions
    def model_predictions(self):
        """Read the deployed model and a test dataset, 
            calculate predictions

        Returns:
            list: Returns a list containing all predictions
        """     
        data = pd.read_csv(self.data_path)
        y = data['exited']
        X = data.drop(['corporation', 'exited'], axis=1)

        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)

        y_pred = model.predict(X)

        return y_pred.tolist()   
        #
        return #return value should be a list containing all predictions

    ##################Function to get summary statistics
    def dataframe_summary():
        #calculate summary statistics here
        return #return value should be a list containing all summary statistics

    ##################Function to get timings
    def execution_time():
        #calculate timing of training.py and ingestion.py
        return #return a list of 2 timing values in seconds

    ##################Function to check dependencies
    def outdated_packages_list():
        #get a list of 
        pass

    def run(self):
        self.model_predictions()
        self.dataframe_summary()
        self.execution_time()
        self.outdated_packages_list()





    
