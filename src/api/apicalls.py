"""
This file is responsible for the deployment on the 
    trained model into pikle.

Name: Felipe Lana Machado
Date: 31/08/2022
"""

import os
import json
import requests

from src.utils.projects_paths import BASE_PATH


#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000/"

with open('config.json','r') as f:
    config = json.load(f)


def responses(URL):
    response1 = requests.post(URL+'/prediction?input_data=testdata/testdata.csv').content
    response2 = requests.get(URL+'/scoring').content
    response3 = requests.get(URL+'/summarystats').content
    response4 = requests.get(URL+'/diagnostics').content

    return [response1, response2, response3, response4]

def api_write(response_all):
    with open(os.path.join(BASE_PATH, config['output_model_path'], 'api_returns.txt'),'w') as file:
        file.write(str(response_all))

if __name__ == '__main__':
    resp = responses(URL)
    api_write(resp)



