# Introduction
print("Welcome to the Tip Calculator!")

# Get user input for the bill amount, tip percentage, and number of people
bill_amount = float(input("Enter the total bill amount: $"))
tip_percentage = int(input("Enter the tip percentage (e.g., 10, 15, 20): "))
number_of_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the tip and total amount
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount

# Calculate each person's share
amount_per_person = total_amount / number_of_people

# Display the results
print("\n--- Bill Summary ---")
print(f"Bill Amount: ${bill_amount:.2f}")
print(f"Tip Percentage: {tip_percentage}%")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
print(f"Each person pays: ${amount_per_person:.2f}")