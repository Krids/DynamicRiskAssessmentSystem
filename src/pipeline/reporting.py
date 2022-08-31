"""
This file is responsible for the reporting of the
    confusion matrix in the trained model.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import logging as log
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt
import json
import os

from src.pipeline.pipeline import Pipeline
from src.utils.projects_paths import BASE_PATH, CONFIG_FILE

from src.pipeline.diagnostics import DiagnosticsPipeline


class ReportingPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.dataset_csv_path = os.path.join(
            BASE_PATH, config['output_folder_path'])
        self.metrics_path = os.path.join(
            BASE_PATH, config['output_metrics_path'])
        self.test_data_path = os.path.join(BASE_PATH, config['test_data_path'])

    def score_model(self):
        """Calculate a confusion matrix using the test 
            data and the deployed model and write the confusion 
            matrix to the workspace
        """
        diagnostics = DiagnosticsPipeline()
        y_pred = diagnostics.model_predictions()

        data = pd.read_csv(os.path.join(self.test_data_path, 'testdata.csv'))
        y_true = data['exited']

        confusion_mat = confusion_matrix(y_true, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=confusion_mat)
        disp.plot()
        log.info(f'Savind confusion matrix in {self.metrics_path}')
        plt.savefig(os.path.join(self.metrics_path, 'confusionmatrix.png'))

    def run(self):
        self.score_model()
