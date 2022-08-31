"""
This file is responsible for the deployment on the 
    trained model into pikle.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import os
import shutil
import json

from src.utils.projects_paths import BASE_PATH, CONFIG_FILE


class Deployment:

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        self.dataset_csv_path = os.path.join(
            BASE_PATH, config['output_folder_path'])
        self.prod_deployment_path = os.path.join(
            BASE_PATH, config['prod_deployment_path'])
        ingested_files_path = os.path.join(
            self.dataset_csv_path, 'ingestedfiles.txt')
        model_path = os.path.join(
            BASE_PATH, config['output_model_path'], 'trainedmodel.pkl')
        score_path = os.path.join(
            BASE_PATH, config['output_model_path'], 'latestscore.txt')

        self.files = [ingested_files_path, model_path, score_path]

        if not os.path.exists(self.prod_deployment_path):
            os.makedirs(self.prod_deployment_path)

    def store_model_into_pickle(self):
        """Copy the latest pickle file, the latestscore.txt value, 
            and the ingestfiles.txt file into the deployment directory
        """

        for file in self.files:
            print(f"Copying: {file}")
            if os.path.isfile(file):
                shutil.copy(src=file, dst=os.path.join(
                    self.prod_deployment_path, file.split('/')[-1]))
            else:
                pass
