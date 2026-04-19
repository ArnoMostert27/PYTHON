# 10-11 Save Favorite Number

import json

number = input("What is your favorite number? ")

with open("favorite_number.json", "w") as file:
    json.dump(number, file)

print("Saved!")