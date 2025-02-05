books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick", "Pride and Prejudice"]


membership_limits = {
    "Regular": 2,
    "Premium": 5,
    "VIP": float('inf') 
}

while True:
    print("\n📚 Welcome to the Library System!")
    print("Available Books:")
    

    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")

   
    name = input("\nEnter your name: ")
    membership = input("Enter your membership type (Regular/Premium/VIP): ").capitalize()
    
    if membership not in membership_limits:
        print("❌ Invalid membership type. Try again!")
        continue  

    max_books = membership_limits[membership]

    try:
        books_to_borrow = int(input("How many books would you like to borrow? "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue 

   
    if books_to_borrow > max_books:
        print(f"❌ Sorry {name}, as a {membership} member, you can borrow only {max_books} books.")
    else:
        print(f"✅ {name}, you have successfully borrowed {books_to_borrow} book(s)! Enjoy reading! 📖")

    exit_choice = input("\nDo you want to exit? (yes/no): ").lower()
    if exit_choice == "yes":
        print("📕 Thank you for using the library system! Goodbye!")
        break 
