import os
from flask import Flask, request
from src.api.apicalls import BASE_PATH
from src.pipeline.diagnostics import DiagnosticsPipeline
from src.pipeline.pipeline import Pipeline
from src.pipeline.scoring import Scoring

class ApiPipeline(Pipeline):
    def __init__(self) -> None:
        super().__init__()
        self.diagnostics = DiagnosticsPipeline()
        self.scoring = Scoring()

        self.app = Flask(__name__)
        self.app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'


        @self.app.route("/prediction", methods=['POST', 'OPTIONS'])
        def __predict():
            return self.predict()


        @self.app.route("/scoring", methods=['GET', 'OPTIONS'])
        def __scoring():
            return self.score()


        @self.app.route("/summarystats", methods=['GET', 'OPTIONS'])
        def __summary():
            return self.summary()


        @self.app.route("/diagnostics", methods=['GET', 'OPTIONS'])
        def __diagnostics():
            return self.diagnose()

    def predict(self):
        """Calls the prediction function

        Returns:
            _type_: Returns the prediction outputs
        """
        data_path = request.args.get('datapath')
        y_pred = self.diagnostics.model_predictions(data_path=data_path)

        return str(y_pred)

    def score(self):
        """Check the score of the deployed model

        Returns:
            double: Returns a single F1 score number
        """
        data_path = request.args.get('datapath')
        score = self.scoring.score_model(data_path=data_path)
        return str(score)

    def summary(self):
        """Check means, medians, and modes 
            for each column

        Returns:
            list: Returns a list of all calculated summary statistics
        """
        data_path = request.args.get('datapath')
        summary = self.diagnostics.dataframe_summary(data_path=data_path)
        return str(summary)

    def diagnose(self):
        """Check timing and percent NA values

        Returns:
            dict: Returns a value for all diagnostics
        """
        data_path = request.args.get('datapath')
        missing = self.diagnostics.missing_data(data_path=data_path)
        runtimes = self.diagnostics.execution_time()
        outdated_packages_ = self.diagnostics.outdated_packages_list()

        output = {
            'missing values (%)': missing,
            'Runtimes': runtimes,
            'Outdated packages': outdated_packages_
        }
        return str(output)


    def run(self):
        self.app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
