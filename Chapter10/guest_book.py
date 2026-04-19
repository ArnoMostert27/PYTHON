# 10-5 Guest Book

names = []

while True:
    name = input("Enter your name (or 'quit'): ")

    if name == "quit":
        break

    names.append(name)

with open("guest_book.txt", "w") as file:
    for n in names:
        file.write(n + "\n")

print("Guest book saved.")