"""
This file is responsible for the training the 
Logistic Regression Model in training data.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json

from src.pipeline.pipeline import Pipeline
from src.utils.projects_paths import BASE_PATH, CONFIG_FILE


class TrainingPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.dataset_csv_path = os.path.join(
            BASE_PATH, config['output_folder_path'])
        self.model_path = os.path.join(BASE_PATH, config['output_model_path'])

    def train_model(self):
        """This function is used for training the logistic regression model.
        """

        df = pd.read_csv(os.path.join(self.dataset_csv_path, 'finaldata.csv'))
        X = df.loc[:, ['lastmonth_activity',
                       'lastyear_activity', 'number_of_employees']]
        y = df['exited']
        X_train, _, y_train, _ = train_test_split(X, y, random_state=10)

        logit = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                                   multi_class='warn', n_jobs=None, penalty='l2',
                                   random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                                   warm_start=False)

        model = logit.fit(X_train, y_train)

        print(f"Saving trained model in {self.model_path} folder")
        pickle.dump(model, open(os.path.join(
            self.model_path, 'trainedmodel.pkl'), 'wb'))
