def check_password(password):

    if (len(password) >= 8 and password.isalpha()):
        print("Your password is good")

    else:
        print("Password is bad")
# program that checks passwordz


check_password("pas322sword")
