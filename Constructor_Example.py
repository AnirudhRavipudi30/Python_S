class Car:
    def __init__(self, brand, model, color):
        self.brand = brand  # Instance attribute
        self.model = model
        self.color = color
        print(f"🚗 A new car {self.brand} {self.model} ({self.color}) has been created!")

# Creating Objects (Constructor automatically runs)
car1 = Car("BMW", "M5 CS", "Green")
car2 = Car("Audi", "RS7", "Blue")