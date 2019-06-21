from ticket_key import search_ticket


def welcome_text():
    print(f"""
    👩‍🚀 myJIRA Explorer 

    [1] Search Ticket
    [2] Current Sprint
    """)


def run():
    welcome_text()
    while True:
        user_command = input(f'>>> ')
        if user_command == str(1):
            search_ticket()
            break
        if user_command == str(2):
            print('Feature not ready yet!')
            # break
        else:
            pass


run()
