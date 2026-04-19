# 9-15 Lottery Analysis

import random

lottery = [1, 2, 3, 4, 5, "A", "B", "C", "D", "E"]

my_ticket = [1, "A", 3, "D"]

attempts = 0
winner = False

while not winner:
    attempts += 1
    pick = random.sample(lottery, 4)

    if pick == my_ticket:
        winner = True

print(f"It took {attempts} attempts to win!")
print("Winning ticket:", my_ticket)