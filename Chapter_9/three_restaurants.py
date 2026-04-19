# 9-2 Three Restaurants

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

r1 = Restaurant("Pizza Palace", "Italian")
r2 = Restaurant("Sushi World", "Japanese")
r3 = Restaurant("Burger Hub", "American")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()