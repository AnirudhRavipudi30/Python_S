#Instance attributes
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute
        self.color = color  # Instance attribute

# Creating Objects
car1 = Car("BMW", "M5 CS", "Green")
car2 = Car("Audi", "RS7", "Blue")

print(car1.brand)  # ✅ Output: BMW
print(car2.color)  # ✅ Output: Blue