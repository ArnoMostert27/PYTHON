# String tests
name = "Arno"

print(name == "Arno")  # True
print(name != "John")  # True

# lower() test
print(name.lower() == "arno")  # True
print(name.lower() == "ARNO")  # False

# Numerical tests
age = 20

print(age == 20)   # True
print(age != 18)   # True
print(age > 18)    # True
print(age < 18)    # False
print(age >= 20)   # True
print(age <= 19)   # False

# AND / OR tests
print(age > 18 and age < 30)  # True
print(age < 18 or age == 20)  # True

# List tests
cars = ['bmw', 'audi', 'toyota']

print('bmw' in cars)      # True
print('ford' in cars)     # False
print('ford' not in cars) # True