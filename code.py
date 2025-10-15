## Imports and basic variables
import time
import math

## user data and core functions
user_data = {
    "Guest": {
        "password": "Password",
        "permrank": "Guest"
    },
    "Wesley": {
        "password": "placeholder",
        "permrank": "Operator"
    }
}

def Login():
    print("Dumb .PY OS\nAll inputs are case sensitive!")
    while True:
        user = input("Username: ")
        passcheck = input("Password: ")
        if user in user_data and passcheck == user_data[user]["password"]:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.\n")

