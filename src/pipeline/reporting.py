"""
This file is responsible for the execution of this script.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

from src.pipeline.pipeline import Pipeline
from src.utils.projects_paths import CONFIG_FILE

class ReportingPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE,'r') as f:
            config = json.load(f) 

        dataset_csv_path = os.path.join(config['output_folder_path']) 

    def score_model(self):
        #calculate a confusion matrix using the test data and the deployed model
        #write the confusion matrix to the workspace
        pass


    def run(self):
        self.score_model()
