import requests
import config

headers = {
    "Authorization": "Bearer" + config.api_token
}


def get_response_json():
    global send_request
    url = f'https://{config.your_domain}.atlassian.net/rest/api/3/filter/12371/columns'

    send_request = requests.get(
        url, headers=headers, auth=(config.user, config.api_token))
    # response_json = send_request.json()


# def find_params():
#     global ticket_key, ticket_title, ticket_status, ticket_reporter_name
#     ticket_key = response_json['key']
#     ticket_title = response_json['fields']['summary']
#     ticket_status = response_json['fields']['status']['name']
#     ticket_reporter_name = response_json['fields']['creator']['displayName']

#     global ticket_assignee_name
#     ticket_assignee = response_json['fields']['assignee']
#     if ticket_assignee is None:
#         ticket_assignee_name = 'None'
#     else:
#         ticket_assignee_name = ticket_assignee['displayName']

#     global sprint_name
#     sprint = response_json['fields']['customfield_10115']
#     if sprint is None:
#         sprint_name = 'None'
#     else:
#         sprint_name = []
#         for i in sprint:
#             find_sprint_names = i.split("name=")[1].split(",")[0]
#             sprint_name.append(find_sprint_names)
#         sprint_name.sort(reverse=True)
#         sprint_name = sprint_name[0]

#     global epic_key
#     epic = response_json['fields']['customfield_10005']
#     if epic is None:
#         epic_key = 'None'
#     else:
#         epic_key = epic


def run():
    get_response_json()

    print(send_request)


run()
