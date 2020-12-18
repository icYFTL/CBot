import requests
import json
from core import config

def get_event(id) -> dict:
    return json.loads(requests.get(f'https://ctftime.org/api/v1/events/{id}/').text)

def get_team(id) -> dict:
    return json.loads(requests.get(f'https://icyftl.ru/ctftime/teams/get/team/{id}/id').text)
