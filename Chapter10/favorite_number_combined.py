# 10-12 Combined Version

import json

filename = "favorite_number.json"

try:
    with open(filename, "r") as file:
        number = json.load(file)
        print(f"I know your favorite number! It's {number}.")
except FileNotFoundError:
    number = input("What is your favorite number? ")

    with open(filename, "w") as file:
        json.dump(number, file)

    print("Stored your number!")