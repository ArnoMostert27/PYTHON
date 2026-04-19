# Create a list of numbers from 1 to 9
numbers = list(range(1, 10))

# Loop through each number
for number in numbers:
    # Check for special cases
    if number == 1:
        print("1st")  # 1 ends with 'st'
    elif number == 2:
        print("2nd")  # 2 ends with 'nd'
    elif number == 3:
        print("3rd")  # 3 ends with 'rd'
    else:
        # All other numbers end with 'th'
        print(f"{number}th")