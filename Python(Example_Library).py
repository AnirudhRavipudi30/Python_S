# Available books in the library
books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick", "Pride and Prejudice"]

# Membership borrowing limits
membership_limits = {
    "Regular": 2,
    "Premium": 5,
    "VIP": float('inf')  # Unlimited books
}

while True:
    print("\n📚 Welcome to the Library System!")
    print("Available Books:")
    
    # 1️⃣ Display available books using a FOR loop
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")

    # 2️⃣ Get user input
    name = input("\nEnter your name: ")
    membership = input("Enter your membership type (Regular/Premium/VIP): ").capitalize()
    
    if membership not in membership_limits:
        print("❌ Invalid membership type. Try again!")
        continue  # Restart the loop if membership type is invalid

    max_books = membership_limits[membership]

    try:
        books_to_borrow = int(input("How many books would you like to borrow? "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue  # Restart if input is not a number

    # 3️⃣ Use IF condition to check borrowing limits
    if books_to_borrow > max_books:
        print(f"❌ Sorry {name}, as a {membership} member, you can borrow only {max_books} books.")
    else:
        print(f"✅ {name}, you have successfully borrowed {books_to_borrow} book(s)! Enjoy reading! 📖")

    # 4️⃣ Ask if the user wants to continue
    exit_choice = input("\nDo you want to exit? (yes/no): ").lower()
    if exit_choice == "yes":
        print("📕 Thank you for using the library system! Goodbye!")
        break  # Exit the while loop