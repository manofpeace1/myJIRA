import requests
import config


def get_response_json():
    global response_json
    component = input(">>> ADS/DAT/etc: ")
    key_number = input(">>> Key Number: ")
    url = f'https://{config.your_domain}.atlassian.net/rest/api/3/issue/{component}-{key_number}'

    send_request = requests.get(
        url, auth=(config.user, config.api_token))
    response_json = send_request.json()

    return response_json


def find_params():
    global ticket_key, ticket_title, ticket_status, ticket_reporter_name
    ticket_key = response_json['key']
    ticket_title = response_json['fields']['summary']
    ticket_status = response_json['fields']['status']['name']
    ticket_reporter_name = response_json['fields']['creator']['displayName']

    global ticket_assignee, ticket_assignee_name
    ticket_assignee = response_json['fields']['assignee']
    if ticket_assignee is None:
        ticket_assignee_name = 'None'
    else:
        ticket_assignee_name = ticket_assignee['displayName']

    global sprint, sprint_name
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

    global epic, epic_key
    epic = response_json['fields']['customfield_10005']
    if epic is None:
        epic_key = 'None'
    else:
        epic_key = epic


def run():
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
    run()


run()
