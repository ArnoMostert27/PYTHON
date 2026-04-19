# 9-14 Lottery

import random

lottery = [1, 2, 3, 4, 5, "A", "B", "C", "D", "E"]

winning_ticket = random.sample(lottery, 4)

print("Winning ticket is:")
print(winning_ticket)