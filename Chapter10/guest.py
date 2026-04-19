# 10-4 Guest

name = input("Enter your name: ")

with open("guest.txt", "w") as file:
    file.write(name)

print("Name saved to guest.txt")