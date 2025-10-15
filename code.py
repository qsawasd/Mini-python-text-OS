## Imports and basic variables
import time
import math
logged_in = False
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
    print("Dumb .PY OS\nAll inputs here are case sensitive!")
    while True:
        user = input("Username: ")
        passcheck = input("Password: ")
        if user in user_data and passcheck == user_data[user]["password"]:
            time.sleep(2)
            print("Login successful!")
            logged_in = True
            break
        else:
            time.sleep(2)
            print("Invalid username or password. Please try again.\n")
def signout():
    confirm = str(input("Are you sure you would like to sign out? yes/no   "))
    if confirm.lower() in ["yes","y"]:
        time.sleep(2)
        print("Signed out!")
        logged_in = False
        break
    else:
        print("Logout canceled")
        break


## Apps
def Credits():
    print("Human creators:\n - Wesley Burkholder\n\nNon-human resources:\n - Bing Copilot\n - Github\n")
    break


## Main Program
while True:
    Login()
    while logged_in == True:
        print("What app would you like to use?")
        print(" - Credits\n - ")
        print(" - Log out")
        action = str(input(""))
        if lower.action() in ["credits"]:
            Credits()
        if lower.action() in ["logout", "log out", "log-out", "sign out"]:
            signout()
        

    













    
