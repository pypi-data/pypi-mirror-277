import requests

def test_add_one(num):
    return num + 1

def test_request():
    return requests.get('https://google.com').status_code