import re


def strong_password(password):
    if re.match(r'[a-zA-Z0-9]{8,}', password):
        print('You have chosen a strong password')
    else:
        print('Your password is weak')


user_password = input()

try:
    strong_password(user_password)
except TypeError:
    print('You did not enter a string')
