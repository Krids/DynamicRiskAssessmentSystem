"""
This file is responsible for the training pipeline
that includes training the model, scoring and deployment.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import os
import pandas as pd
from src.pipeline.pipeline import Pipeline
from src.pipeline.training import Training
from src.pipeline.scoring import Scoring
from src.pipeline.deployment import Deployment


class TrainingPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()
        self.training = Training()
        self.scoring = Scoring()
        self.deployment = Deployment()

    def run(self):
        self.training.train_model()
        self.scoring.score_model()
        self.deployment.store_model_into_pickle()
