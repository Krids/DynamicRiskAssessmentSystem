# Dynamic Risk Assessment System

## Background

Imagine that you're the Chief Data Scientist at a big company that has 10,000 corporate clients. Your company is extremely concerned about attrition risk: the risk that some of their clients will exit their contracts and decrease the company's revenue. They have a team of client managers who stay in contact with clients and try to convince them not to exit their contracts. However, the client management team is small, and they're not able to stay in close contact with all 10,000 clients.

The company needs you to create, deploy, and monitor a risk assessment ML model that will estimate the attrition risk of each of the company's 10,000 clients. If the model you create and deploy is accurate, it will enable the client managers to contact the clients with the highest risk and avoid losing clients and revenue.

Creating and deploying the model isn't the end of your work, though. Your industry is dynamic and constantly changing, and a model that was created a year or a month ago might not still be accurate today. Because of this, you need to set up regular monitoring of your model to ensure that it remains accurate and up-to-date. You'll set up processes and scripts to re-train, re-deploy, monitor, and report on your ML model, so that your company can get risk assessments that are as accurate as possible and minimize client attrition.


<img src="docs/images/a_dynamic_risk_assessment_system.png">

The third project [ML DevOps Engineer Nanodegree](https://www.udacity.com/course/machine-learning-dev-ops-engineer-nanodegree--nd0821) by Udacity. Instructions are available in udacity's [repository](https://github.com/udacity/nd0821-c3-starter-code/tree/master/starter)

## Description
Project: A Dynamic Risk Assessment System. 

## Prerequisites
- Python and Jupyter Notebook are required
- Github account to use Github Actions for CI
- Linux environment may be needed within windows through WSL2

## Dependencies
This project dependencies is available in the ```requirements.txt``` file.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies from the ```requirements.txt```. Its recommended to install it in a separate virtual environment.

```bash
pip install -r requirements.txt
```

## Project Structure
```bash
📦Census Bureal Classification
 ┣ 
 ┣ 📂.github
 ┃ ┗ 📂workflows
 ┃ ┃ ┗ 📜main.yml           # Github Action yml file
 ┣ 📂data                   # Dataset folder
 ┃ ┣ 📂raw
 ┃ ┗ 📂processed   
 ┣ 📂docs      
 ┃ ┣ 📂metrics                # Model metrics
 ┃ ┣ 📂models                 # Trained serialized models
 ┃ ┗ 📂plots                  # Saved figures
 ┣ 📂notebooks              # EDA notebook
 ┣ 📂screenshots            # Screenshots needed for the project other resources
 ┣ 📂src                
 ┃ ┣ 📂app                  # FastAPI folder
 ┃ ┣ 📂pipeline             # Model pipeline architecture and train functions
 ┃ ┣ 📂tests                # Testing functions
 ┃ ┣ 📜config.py            # Config file for the project
 ┃ ┣ 📜request_heroku.py    # Request from API deployed on Heroku
 ┃ ┗ 📜training.py          # Train model and generate metrics and figures
 ┣ 📜Aptfile                # Used for integrating DVC with Heroku
 ┣ 📜model_card.md          # Model card includes info about the model 
 ┣ 📜Procfile               # Procfile for Heroku
 ┣ 📜README.md              
 ┗ 📜requirements.txt       # Projects required dependencies
```
## Usage
The config file contains ```MODEL``` variable with a  ```RandomForestClassifier```. The model with a set of parameters for the grid search ```PARAM_GRID```. You can your own model with the parameters needed. The ```SLICE_COLUMNS``` variable is responsible for the columns for slice evaluation.

1- Start training
```bash
cd src
python training.py
```
This saves a seralized model, generates evaluation metrics, slice evaluation metrics and figures,

2- Start FastAPI app
```bash
cd src
uvicorn app.api:app --reload
```

3- FastAPI app documentation to test the API from the browser
```
http://127.0.0.1:8000/docs
```

<img src="screenshots/example.png">

4- Testing the project
```bash
cd src
pytest -vv
```
5- Showing tracked files with DVC
```bash
dvc dag
```

<img src="screenshots/dvc_dag.png">

6- CI using github action will be triggered upon pushing to github
```bash
git push
```

7- CD is enabled from within Heroku app settings

<img src="screenshots/continuous_deployment.png">

8- Starting the app on Heroku

<img src="screenshots/live_get.png">

9- Test deployment on Heroku, demo post request
```bash
python request_heroku.py
```

<img src="screenshots/live_post.png">

## License
Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See ```LICENSE``` for more information.

## Resources

- Data and Modeling
  - [An article about the data and its ML application](https://medium.com/analytics-vidhya/machine-learning-application-census-income-prediction-868227debf12)
- ML Testing
  - [Made with ML Testing Lesson](https://madewithml.com/courses/mlops/testing/)
  - [Jeremy Jordan Article](https://www.jeremyjordan.me/testing-ml/)
  - [Eugeneyan Article about ML Testing](https://eugeneyan.com/writing/testing-ml/)
  - [Eugeneyan Article about Python Automation and Collaboration](https://eugeneyan.com/writing/setting-up-python-project-for-automation-and-collaboration/)
  - [mCoding video for automated testing](https://www.youtube.com/watch?v=DhUpxWjOhME)
- FastAPI
  - [Made with ML API Lesson](https://madewithml.com/courses/mlops/api/)
  - [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- Github Actions
  - [Made with ML CI/CD Lesson](https://madewithml.com/courses/mlops/cicd/)
  - [DVC with Github Actions](https://github.com/iterative/setup-dvc)
  - [AWS Credentials with Github Actions #1](https://github.com/marketplace/actions/configure-aws-credentials-action-for-github-actions#sample-iam-role-cloudformation-template)
  - [AWS Credentials with Github Actions #2](https://stackoverflow.com/questions/58643905/how-aws-credentials-works-at-github-actions)
- Heroku
  - [Procfile Tutorial](https://devcenter.heroku.com/articles/procfile)
  - [Integrate DVC with Heroku](https://ankane.org/dvc-on-heroku)