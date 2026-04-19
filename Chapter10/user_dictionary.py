# 10-13 User Dictionary

import json

user = {}

user["first_name"] = input("First name: ")
user["last_name"] = input("Last name: ")
user["age"] = input("Age: ")

with open("user.json", "w") as file:
    json.dump(user, file)

with open("user.json", "r") as file:
    data = json.load(file)

print("\nUser Data:")
for key, value in data.items():
    print(f"{key}: {value}")