# 9-3 Users Class

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, Age: {self.age}, City: {self.city}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

u1 = User("Arno", "Mostert", 20, "Pretoria")
u2 = User("John", "Smith", 25, "London")

u1.describe_user()
u1.greet_user()

u2.describe_user()
u2.greet_user()