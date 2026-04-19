# List of current users
current_users = ["admin", "jaden", "alex", "mike", "sarah"]

# List of new users trying to register
new_users = ["john", "Alex", "mike", "linda", "steve"]

# Create a new list with all current users in lowercase
# This helps us compare usernames without case sensitivity
current_users_lower = [user.lower() for user in current_users]

# Loop through each new user
for user in new_users:
    # Convert the new username to lowercase and check if it exists
    if user.lower() in current_users_lower:
        # If it exists, username is taken
        print(f"{user} is already taken, please choose another username.")
    else:
        # If not, username is available
        print(f"{user} is available.")