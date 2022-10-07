import requests
from heapq import heappush, heappop

BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
X_AUTH_TOKEN = '1dbaa65a9792edf0e1d05e7ebce0f51d'


def start():
    headers = {
        'X-Auth-Token': X_AUTH_TOKEN,
    }

    json_data = {
        'problem': 1,
    }

    response = requests.post(BASE_URL + '/start', headers=headers, json=json_data).json()

    return response


def waiting_line(AUTH_KEY):
    headers = {
    'Authorization': AUTH_KEY,
    'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/waiting_line', headers=headers).json()
    
    return response


def game_result(AUTH_KEY):
    headers = {
    'Authorization': AUTH_KEY,
    'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/game_result', headers=headers).json()

    return response


def user_info(AUTH_KEY):
    headers = {
    'Authorization': AUTH_KEY,
    'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/user_info', headers=headers).json()

    return response


def match(AUTH_KEY, pairs):
    headers = {
    'Authorization': AUTH_KEY,
    }

    json_data = {
        'pairs': pairs,
    }

    response = requests.put(BASE_URL + '/match', headers=headers, json=json_data).json()

    return response


def change_grade(AUTH_KEY, commands):
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    json_data = {
        'commands': commands,
    }

    response = requests.put(BASE_URL + '/change_grade', headers=headers, json=json_data).json()

    return response


def score(AUTH_KEY):
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/score', headers=headers).json()
    
    return response

info = start()
auth_key = info['auth_key']
problem = info['problem']
t = info['time']
if problem == 1:
    grade = [5000]*31
else:
    grade = [5000]*901
wait_line = []
while True:
    waiting_users = waiting_line(auth_key)['waiting_line']
    for wu in waiting_users:
        heappush(wait_line, (wu['from'], wu['id']))