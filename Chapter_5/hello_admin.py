# Create a list of usernames
users = ["admin", "jaden", "alex", "mike", "sarah"]

# Loop through each user in the list
for user in users:
    # Check if the current user is 'admin'
    if user == "admin":
        # Special message for admin
        print("Hello admin, would you like to see a status report?")
    else:
        # Generic message for all other users
        print(f"Hello {user}, thank you for logging in again.")