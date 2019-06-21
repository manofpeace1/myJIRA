from re import split
from requests import get
import config


def get_response_json():
    global response_json
    user_input_key = input('\n👩‍🚀 JIRA Ticket Key >>> ')
    if '-' not in user_input_key:
        user_input_key_split = split('(\d+)', user_input_key)
        user_input_key = f'{user_input_key_split[0]}-{user_input_key_split[1]}'
    url = f'https://{config.your_domain}.atlassian.net/rest/api/3/issue/{user_input_key}'
    send_request = get(
        url, auth=(config.user, config.api_token))
    response_json = send_request.json()


def find_params():
    global ticket_key, ticket_title, ticket_status, ticket_reporter_name
    ticket_key = response_json['key']
    ticket_title = response_json['fields']['summary']
    ticket_status = response_json['fields']['status']['name']
    ticket_reporter_name = response_json['fields']['creator']['displayName']

    global ticket_assignee_name
    ticket_assignee = response_json['fields']['assignee']
    if ticket_assignee is None:
        ticket_assignee_name = 'None'
    else:
        ticket_assignee_name = ticket_assignee['displayName']

    global sprint_name
    sprint = response_json['fields']['customfield_10115']
    if sprint is None:
        sprint_name = 'None'
    else:
        sprint_name = []
        for i in sprint:
            find_sprint_names = i.split("name=")[1].split(",")[0]
            sprint_name.append(find_sprint_names)
        sprint_name.sort(reverse=True)
        sprint_name = sprint_name[0]

    global epic_key
    epic = response_json['fields']['customfield_10005']
    if epic is None:
        epic_key = 'None'
    else:
        epic_key = epic


def search_ticket():
    get_response_json()
    find_params()

    print(f"""
    =============================================================
    {ticket_key}
    {ticket_title}

    - Status: {ticket_status}
    - Assignee: {ticket_assignee_name}
    - Reporter: {ticket_reporter_name}
    - Sprint: {sprint_name}
    - Epic: {epic_key}
    =============================================================
    """)
    search_ticket()
