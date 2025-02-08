class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"🚗 A new car {self.brand} {self.model} has been created!")

    def __del__(self):
        print(f"❌ The car {self.brand} {self.model} has been removed from memory!")

# Creating an Object
car1 = Car("Mercedes", "AMG GT")

# Deleting Object (Destructor is called automatically)
del car1