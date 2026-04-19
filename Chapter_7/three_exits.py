# 7-6 Three Exits (different loop control methods)

active = True

while active:
    topping = input("Enter pizza topping (or 'quit'): ")

    # Exit method 1: break statement
    if topping == "quit":
        break

    print(f"Adding {topping} to pizza.")

# Alternative controlled loop example (active variable)
active = True

while active:
    age = input("Enter age (or 'quit'): ")

    if age == "quit":
        active = False
    else:
        age = int(age)

        if age < 3:
            print("Free ticket")
        elif age <= 12:
            print("$10 ticket")
        else:
            print("$15 ticket")