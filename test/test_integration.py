import json
from pathlib import Path

import pytest
import requests

from deployment.streaming.lambda_function import lambda_handler


def read_json(file):
    test_path = Path(__file__).parent
    with open(test_path / file, "rt", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def global_variables():
    event = read_json("event.json")
    url = "http://localhost:8080/2015-03-31/functions/function/invocations"

    predictions = [
        {
            "name": "Russell Jimenez",
            "city": "Jenniferton",
            "phone": "(377)489-0032x64590",
            "id": "2bf54686-b801-49d7-9194-9770b7aff96c",
        }
    ]

    expected_response = {
        "statusCode": 200,
        "body": "SUCCESS",
        "predictions": predictions,
    }

    lst = [url, event, expected_response]

    return lst


def docker_lamda_call(url, event, timeout=20):
    actual_response = requests.post(url, json=event, timeout=timeout)
    return actual_response


def test_docker_lambda(global_variables):

    url = global_variables[0]
    event = global_variables[1]
    expected_response = global_variables[2]

    response = docker_lamda_call(url, event)
    assert response.status_code == 200
    assert response.json() == expected_response

    response_func = lambda_handler(event, "context")
    assert response_func == expected_response
