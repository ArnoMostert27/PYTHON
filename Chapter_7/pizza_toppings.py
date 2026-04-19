# 7-4 Pizza Toppings

topping = ""

while topping != "quit":
    topping = input("Enter pizza topping (or 'quit' to stop): ")

    if topping != "quit":
        print(f"I will add {topping} to your pizza.")