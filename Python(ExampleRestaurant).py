# Restaurant Menu with Prices
menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Pasta": 7.49,
    "Salad": 4.99,
    "Soda": 1.99
}

# Welcome Message
print("🍽️ Welcome to the Restaurant Order System!")

while True:  # Keep the system running until the user decides to exit
    print("\n📜 Menu:")
    
    # 1️⃣ Display menu using a FOR loop
    for dish, price in menu.items():
        print(f"{dish}: ${price:.2f}")

    # 2️⃣ Ask for user input (order)
    order = input("\nEnter the dish you want to order (or type 'exit' to finish): ").capitalize()

    if order.lower() == "exit":
        print("🛑 Thank you for visiting! Have a great day! 🍽️")
        break  # Exit the loop if user types 'exit'

    # 3️⃣ Use IF condition to check dish availability
    if order in menu:
        print(f"✅ {order} has been added to your order. Price: ${menu[order]:.2f}")
    else:
        print("❌ Sorry, that dish is not available. Please choose from the menu.")