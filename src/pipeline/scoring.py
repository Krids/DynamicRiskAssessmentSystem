"""
This file is responsible for the execution of this script.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json

from src.pipeline.pipeline import Pipeline
from src.utils.projects_paths import CONFIG_FILE


class ScoringPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.dataset_csv_path = os.path.join(config['output_folder_path'])
        self.test_data_path = os.path.join(config['test_data_path'])

    # Function for model scoring

    def score_model():
        # this function should take a trained model, load test data, and calculate an F1 score for the model relative to the test data
        # it should write the result to the latestscore.txt file
        pass
