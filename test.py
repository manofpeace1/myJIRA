import re
import requests
import config


def get_response_json():
    global response_json
    user_input_key = input("\n>>> Ticket Key: ")
    if '-' not in user_input_key:
        user_input_key_split = re.split('(\d+)', user_input_key)
        user_input_key = f'{user_input_key_split[0]}-{user_input_key_split[1]}'
    url = f'https://{config.your_domain}.atlassian.net/rest/api/3/issue/{user_input_key}'
    send_request = requests.get(
        url, auth=(config.user, config.api_token))
    response_json = send_request.json()


def run():
    get_response_json()
    print(response_json)


run()
