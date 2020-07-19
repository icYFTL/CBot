import requests
import json

def get_event(id) -> dict:
    return json.loads(requests.get(f'https://ctftime.org/api/v1/events/{id}/').text)

def get_team(id) -> dict:
    return json.loads(requests.get(f'https://icyftl.ru/ctftime/teams/get/team/{id}/id').text)

def auth() -> requests.session:
    raise NotImplementedError
