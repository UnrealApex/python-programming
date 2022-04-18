def check_password(password):
    digits = 0
    for i in password:
        if i.isdigit():
            digits += 1

    if (len(password) >= 8 and password.isalnum() and digits >= 2):
        print("Your password is good")

    else:
        print("Password is bad")
# program that checks passwordz


check_password("1234password")
