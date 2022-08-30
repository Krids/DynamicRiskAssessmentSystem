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

from src.utils.projects_paths import CONFIG_FILE
from src.pipeline.pipeline import Pipeline

class DeploymentPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        with open(CONFIG_FILE,'r') as f:
            config = json.load(f) 

        self.dataset_csv_path = os.path.join(config['output_folder_path']) 
        self.prod_deployment_path = os.path.join(config['prod_deployment_path']) 


    def store_model_into_pickle(model):
        #copy the latest pickle file, the latestscore.txt value, and the ingestfiles.txt file into the deployment directory
        pass
        
        

