# 🚗 Car Rental System
class CarRental:
    def __init__(self):
        # Dictionary with car models and their rental prices per day
        self.available_cars = {
            "BMW M5 CS": 150,
            "Audi RS7": 140,
            "Mercedes AMG GT": 180,
            "Porsche 911": 200
        }
        self.rented_cars = {}  # Stores rented cars and user details

    # 1️⃣ Function to display available cars
    def display_available_cars(self):
        print("\n🚗 Available Cars for Rent:")
        for car, price in self.available_cars.items():
            print(f"{car} - ${price}/day")

    # 2️⃣ Function to rent a car
    def rent_car(self, name, car_model, days):
        if car_model in self.available_cars:
            rental_price = self.available_cars[car_model] * days
            self.rented_cars[name] = (car_model, days, rental_price)
            del self.available_cars[car_model]  # Remove from available list
            print(f"\n✅ {name}, you have rented {car_model} for {days} days. Total Cost: ${rental_price}")
        else:
            print("\n❌ Sorry, the car is not available.")

    # 3️⃣ Function to return a car
    def return_car(self, name):
        if name in self.rented_cars:
            car_model, days, _ = self.rented_cars[name]
            self.available_cars[car_model] = self.rented_cars[name][2] // days  # Restore rental price
            del self.rented_cars[name]  # Remove from rented list
            print(f"\n✅ Thank you, {name}! You have successfully returned {car_model}.")
        else:
            print("\n❌ No record found for this name.")

    # 4️⃣ Function to check rental prices (using **kwargs)
    def check_rental_price(self, **car_models):
        print("\n💰 Rental Prices:")
        for car, days in car_models.items():
            if car in self.available_cars:
                price = self.available_cars[car] * days
                print(f"{car} for {days} days: ${price}")
            else:
                print(f"{car} is not available.")

# 🚀 Main interactive function
def main():
    rental_service = CarRental()

    while True:
        print("\n📌 Car Rental System")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Check Rental Price")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rental_service.display_available_cars()

        elif choice == "2":
            name = input("Enter your name: ")
            car_model = input("Enter the car model you want to rent: ")
            days = int(input("Enter number of days: "))
            rental_service.rent_car(name, car_model, days)

        elif choice == "3":
            name = input("Enter your name to return the car: ")
            rental_service.return_car(name)

        elif choice == "4":
            rental_service.check_rental_price(**{"BMW M5 CS": 3, "Audi RS7": 2})  # Example Query

        elif choice == "5":
            print("🚗 Thank you for using the Car Rental System!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
main()