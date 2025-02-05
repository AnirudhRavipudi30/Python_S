menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Pasta": 7.49,
    "Salad": 4.99,
    "Soda": 1.99
}

print("🍽️ Welcome to the Restaurant Order System!")

while True: 
    print("\n📜 Menu:")
    
  
    for dish, price in menu.items():
        print(f"{dish}: ${price:.2f}")
    order = input("\nEnter the dish you want to order (or type 'exit' to finish): ").capitalize()

    if order.lower() == "exit":
        print("🛑 Thank you for visiting! Have a great day! 🍽️")
        break  


    if order in menu:
        print(f"✅ {order} has been added to your order. Price: ${menu[order]:.2f}")
    else:
        print("❌ Sorry, that dish is not available. Please choose from the menu.")
