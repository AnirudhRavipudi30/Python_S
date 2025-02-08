class Car:
    wheels = 4  # Class attribute (shared by all cars)

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

# Creating Objects
car1 = Car("BMW", "M5 CS")
car2 = Car("Audi", "RS7")

print(car1.wheels)  # ✅ Output: 4
print(car2.wheels)  # ✅ Output: 4

# Changing the class attribute
Car.wheels = 6
print(car1.wheels)  # ✅ Output: 6
print(car2.wheels)  # ✅ Output: 6