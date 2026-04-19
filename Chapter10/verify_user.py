# 10-14 Verify User

import json

filename = "user.json"

def get_new_username():
    username = input("What is your name? ")

    with open(filename, "w") as file:
        json.dump(username, file)

    return username

def greet_user():
    try:
        with open(filename, "r") as file:
            username = json.load(file)

        print(f"Is this you, {username}? (yes/no)")
        response = input()

        if response == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you as {username}.")

    except FileNotFoundError:
        username = get_new_username()
        print(f"We'll remember you as {username}.")

greet_user()