# 3-6 More Guests

guests = ["Elon Musk", "Albert Einstein", "Bill Gates"]

print("We found a bigger table!")

guests.insert(0, "Isaac Newton")
guests.insert(2, "Nikola Tesla")
guests.append("Mark Zuckerberg")

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")