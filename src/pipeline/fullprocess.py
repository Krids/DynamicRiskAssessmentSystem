"""
This file is responsible for the execution of 
    the entire script.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import os
import ast
import glob
import json
import sys
import subprocess
import logging as log
from src.pipeline.pipeline import Pipeline
from src.pipeline.scoring import Scoring
from src.utils.projects_paths import BASE_PATH, CONFIG_FILE


class FullprocessPipelie(Pipeline):

    def __init__(self) -> None:
        super().__init__()

        self.scoring = Scoring()

        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.input_folder_path = os.path.join(
            BASE_PATH, config['input_folder_path'])
        self.ingestedfiles_path = os.path.join(
            BASE_PATH, config['prod_deployment_path'], 'ingestedfiles.txt')
        self.ingesteddata_path = os.path.join(
            BASE_PATH, config['output_folder_path'], 'finaldata.csv')
        self.lastestscore_path = os.path.join(
            BASE_PATH, config['output_metrics_path'], 'latestscore.txt')
        self.model_path = os.path.join(
            BASE_PATH, config['prod_deployment_path'], 'trainedmodel.pkl')

        with open(self.ingestedfiles_path, 'r+') as f:
            self.ingested_files = ast.literal_eval(f.read())

    def run(self):

        # Determine whether the source data folder has files that aren't listed in ingestedfiles.txt
        filenames = glob.glob(self.input_folder_path + "/*.csv")
        new_files = []
        print(filenames)
        for file in filenames:
            print(f"{file} in {self.input_folder_path}")
            if os.path.basename(file) not in self.ingested_files:
                new_files.append(file)
            else:
                pass

        # Deciding whether to proceed, part 1
        # if you found new data, you should proceed. otherwise, do end the process here
        if len(new_files) > 0:
            subprocess.run(['python', 'main.py', '-p', 'ingestion'])
        else:
            sys.exit()

        # Checking for model drift
        # check whether the score from the deployed model is different from the score from the model that uses the newest ingested data
        with open(self.lastestscore_path, 'r') as f:
            latest_score = float(f.read())

        score = self.scoring.score_model(self.ingesteddata_path)

        check_model_drift = score < latest_score

        # Deciding whether to proceed, part 2
        # if you found model drift, you should proceed. otherwise, do end the process here
        if check_model_drift == False:
            print(
                f'NO Model drift. Previous model F1 score was {latest_score}. New model score is {score}.')
            sys.exit()

        else:
            # Re-deployment
            # if you found evidence for model drift, re-run the deployment.py script
            # Retrain and redeploy model
            log.info(f'Model drift has been detected.\n')
            log.info(
                f"Previous model F1 score was {latest_score}. New model score is {score}.\n")
            log.info("Training new model.")
            # Retrain model with latest data
            # Score model on test data
            # Redeploy model
            subprocess.run(['python', 'main.py', '-p', 'training'])

            ##################Diagnostics and reporting
            # run diagnostics.py and reporting.py for the re-deployed model
            # Generate report
            subprocess.run(['python', 'main.py', '-p', 'diagnostics'])

            # Run diagnostics
            subprocess.run(['python', 'main.py', '-p', 'reporting'])
