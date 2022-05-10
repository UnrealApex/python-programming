# TODO: validate if id given is an integer
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
    id = input("Enter an account id")
    if (0 < int(id) < 10):
        main_menu(id)
    else:
        print("Invalid id, try again!")
        get_id()

def main_menu(id):
    print("Main Menu\n\
        1: check balance\n\
        2: withdraw\n\
        3: deposit\n\
        4: exit\n\
          ")
    selection = int(input("Enter your selection here: "))
    if (selection == 1):
        print(eval(f"account_{id}.get_balance()"))
    else if(selection == 2):
        withdraw_amount = float(prompt("Enter the amount of money you would like to withdraw: "))
        eval(f"account_{id}.withdraw({withdraw_amount})")
        print(f"${withdraw_amount} was withdrawed successfully")
        


get_id()
