
"""
This file is responsible for the execution of this script.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import pandas as pd
import numpy as np
import timeit
import os
import json

from src.pipeline.pipeline import Pipeline
from src.utils.projects_paths import CONFIG_FILE

class DiagnosticsPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        ##################Load config.json and get environment variables
        with open(CONFIG_FILE,'r') as f:
            config = json.load(f) 

        self.dataset_csv_path = os.path.join(config['output_folder_path']) 
        self.test_data_path = os.path.join(config['test_data_path']) 

    ##################Function to get model predictions
    def model_predictions():
        #read the deployed model and a test dataset, calculate predictions
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





    
