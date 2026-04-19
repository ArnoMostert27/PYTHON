# Testing different conditions

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

# More tests (at least 10 total)

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)

print("\nIs len(car) < 5? I predict False.")
print(len(car) < 5)

print("\nIs car in ['subaru','bmw']? I predict True.")
print(car in ['subaru','bmw'])

print("\nIs car in ['audi','vw']? I predict False.")
print(car in ['audi','vw'])

print("\nIs car.startswith('s')? I predict True.")
print(car.startswith('s'))

print("\nIs car.endswith('x')? I predict False.")
print(car.endswith('x'))