

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


class TrainingPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.dataset_csv_path = os.path.join(config['output_folder_path'])
        self.model_path = os.path.join(config['output_model_path'])

    # Function for training the model

    def train_model():

        # use this logistic regression for training
        LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                           intercept_scaling=1, l1_ratio=None, max_iter=100,
                           multi_class='warn', n_jobs=None, penalty='l2',
                           random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                           warm_start=False)

        # fit the logistic regression to your data

        # write the trained model to your workspace in a file called trainedmodel.pkl
