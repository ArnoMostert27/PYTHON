# 8-12 Sandwiches (*args)

def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")

make_sandwich("ham", "cheese")
make_sandwich("chicken", "lettuce", "mayo")
make_sandwich("peanut butter", "jam", "banana", "honey")