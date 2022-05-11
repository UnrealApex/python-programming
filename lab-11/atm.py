# TODO: validate if id given is an integer
from account import Account

# for i in range(1, 9):
#   eval(f"account_{i} = Account({i}, 100)")

account_1 = Account(1, 100)
account_2 = Account(2, 100)
account_3 = Account(3, 100)
account_4 = Account(4, 100)
account_5 = Account(5, 100)
account_6 = Account(6, 100)
account_7 = Account(7, 100)
account_8 = Account(8, 100)
account_9 = Account(9, 100)


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
        get_id()
    elif (selection == 2):
        withdraw_amount = float(
            input("Enter the amount of money you would like to withdraw: "))
        eval(f"account_{id}.withdraw({withdraw_amount})")
        print(f"${withdraw_amount} was withdrawed successfully\nYour new balance is {eval('account_'+ id + '.get_balance()')}")
        get_id()
    elif (selection == 3):
        deposit_amount = float(
            input("Enter the amount of money you would like to deposit: "))
        eval(f"account_{id}.deposit({deposit_amount})")
        print(f"${deposit_amount} was deposited  successfully\nYour new balance is {eval('account_' + id + '.get_balance()')}")
        get_id()
    elif (selection == 4):
        exit()
    else:
        print("Error")


get_id()
