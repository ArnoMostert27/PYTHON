# 3-7 Shrinking Guest List

guests = ["Isaac Newton", "Elon Musk", "Nikola Tesla", "Albert Einstein", "Bill Gates", "Mark Zuckerberg"]

print("Only two guests can be invited.")

while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, I can't invite you to dinner.")

print(f"{guests[0]}, you're still invited.")
print(f"{guests[1]}, you're still invited.")

del guests[:]

print(guests)