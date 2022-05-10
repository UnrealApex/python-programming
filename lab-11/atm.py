from account import Account

account_1 = Account(i + 1, 100)
account_2 = Account(i + 1, 100)
account_3 = Account(i + 1, 100)
account_3 = Account(i + 1, 100)
account_4 = Account(i + 1, 100)
account_5 = Account(i + 1, 100)
account_6 = Account(i + 1, 100)
account_7 = Account(i + 1, 100)
account_8 = Account(i + 1, 100)
account_9 = Account(i + 1, 100)

def get_id():
    global id
    id = prompt("Enter an account id")
        if (isinstance(id, str) and 0 < id < 10):
            main_menu(id)
        else:
            print("Invalid id, try again!")
            get_id()

def main_menu(id)
    print("Main Menu\
        1: check balance
        2: withdraw
        3: deposit
        4: exit
          ")
    selection = int(input("Enter your selection here: "))
    if (selection == 1):
        eval(f"account_{id}.get_balance()")
