Car_Info = {
    "BMW 540i": 63000,
    "BMW M850i": 70000,
    "BMW X5 M": 80000,
    "BMW X7 sDrive40i": 100000,
    "BMW M3 Competition": 110000,
    "BMW M4 CS": 120000,
    "Audi R8 V10": 130000,
    "BMW M5 CS": 140000
}

# Customer selects a car
Customer_Selection = input("Please enter the name of the car of your choice: ")

# Check if the car is available
if Customer_Selection in Car_Info:
    base_price = Car_Info[Customer_Selection]
    print(f"The car you have selected is available, and the price is: ${base_price:,}")
else:
    print("We're sorry, the car is no longer available or is not in our inventory!")
    exit()

# Get the customer's credit score
Customer_CScore = int(input("Please enter your Credit Score: "))

# Define interest rates and loan term
loan_term_years = 5  # Loan term (5 years)
loan_term_months = loan_term_years * 12  # Convert to months

if Customer_CScore >= 700:
    discount = 0.05 * base_price  # 5% discount
    final_price = base_price - discount
    interest_rate = 3.5  # Lower interest rate for good credit
    print(f"You are eligible for a 5% discount! New price: ${final_price:,}")
    
elif 640 <= Customer_CScore < 700:
    final_price = base_price  # No discount
    interest_rate = 6.5  # Higher interest rate
    print("Your interest rates will be higher than usual!")

else:
    print("Sorry, you are not eligible for a loan!")
    exit()

# Monthly payment calculation using eval()
loan_calculation = f"({final_price} * ({interest_rate} / 100) / 12) + ({final_price} / {loan_term_months})"
monthly_payment = eval(loan_calculation)

# Display final monthly payment
print(f"Your estimated monthly payment over {loan_term_years} years is: ${monthly_payment:,.2f}")