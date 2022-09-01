"""
This file is responsible for the deployment on the 
    trained model into pikle.

Name: Felipe Lana Machado
Date: 31/08/2022
"""

import os
import json
import requests

BASE_PATH = os.path.abspath('.')
CONFIG_FILE = os.path.join(BASE_PATH, 'src', 'utils', 'config.json')


# Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000"

with open(CONFIG_FILE, 'r') as f:
    config = json.load(f)


def responses(URL):
    response1 = requests.post(
        f'{URL}/prediction?datapath=data/testdata/testdata.csv').content
    response2 = requests.get(
        f'{URL}/scoring?datapath=data/testdata/testdata.csv').content
    response3 = requests.get(
        f'{URL}/summarystats?datapath=data/testdata/testdata.csv').content
    response4 = requests.get(
        f'{URL}/diagnostics?datapath=data/testdata/testdata.csv').content

    responses = {
        'Prediction response': json.loads(response1.decode('utf8').replace("'", '"')),
        'Scoring response': json.loads(response2.decode('utf8').replace("'", '"')),
        'Summary stats response': json.loads(response3.decode('utf8').replace("'", '"')),
        'Diagnostics response': json.loads(response4.decode('utf8').replace("'", '"'))
    }

    return responses


def api_write(response_all):
    with open(os.path.join(BASE_PATH, config['output_model_path'], 'api_returns.json'), 'w') as file:
        file.write(json.dumps(response_all))


if __name__ == '__main__':
    resp = responses(URL)
    api_write(resp)
