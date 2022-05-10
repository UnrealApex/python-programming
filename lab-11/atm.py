from account import Account

account_1 = Account(1 + 2, 100)
account_2 = Account(2 + 1, 100)
account_3 = Account(3 + 1, 100)
account_4 = Account(4 + 1, 100)
account_5 = Account(5 + 1, 100)
account_6 = Account(6 + 1, 100)
account_7 = Account(7 + 1, 100)
account_8 = Account(8 + 1, 100)
account_9 = Account(9 + 1, 100)

def get_id():
    global id
    id = prompt("Enter an account id")
    if (isinstance(id, str) and 0 < id < 10):
        main_menu(id)
    else:
        print("Invalid id, try again!")
        get_id()

def main_menu(id):
    print("Main Menu\
        1: check balance\
        2: withdraw\
        3: deposit\
        4: exit\
          ")
    selection = int(input("Enter your selection here: "))
    if (selection == 1):
        eval(f"account_{id}.get_balance()")

get_id()
