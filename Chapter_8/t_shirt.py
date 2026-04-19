# 8-3 T-Shirt Function

def make_shirt(size, message):
    print(f"The shirt size is {size} and it says '{message}'")

# Positional arguments
make_shirt("M", "Hello World")

# Keyword arguments
make_shirt(size="L", message="Python is fun")