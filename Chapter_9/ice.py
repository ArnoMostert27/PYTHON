# 9-13 Dice

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# 6-sided die
die = Die()
print("6-sided die:")
for _ in range(10):
    print(die.roll_die())

# 10-sided die
die10 = Die(10)
print("\n10-sided die:")
for _ in range(10):
    print(die10.roll_die())

# 20-sided die
die20 = Die(20)
print("\n20-sided die:")
for _ in range(10):
    print(die20.roll_die())