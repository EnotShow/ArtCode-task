import requests
from requests.exceptions import HTTPError


def get_api_data(obj):
    response = requests.get(f'http://127.0.0.1:8000/api/test/v1/search/{obj}/')
    response.raise_for_status()
    jsonResponse = response.json()
    return jsonResponse
