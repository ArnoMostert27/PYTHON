# Create a list with some users
users = ["admin", "jaden", "alex"]

# Check if the list is not empty
if users:
    # Loop through users and print greeting
    for user in users:
        print(f"Hello {user}")
else:
    # If list is empty, print this message
    print("We need to find some users!")

# Now empty the list to test the condition
users = []

# Check again if the list is empty
if users:
    for user in users:
        print(f"Hello {user}")
else:
    # This should now run because the list is empty
    print("We need to find some users!")