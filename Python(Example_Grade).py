# Welcome message
print("📚 Welcome to the Student Grade Calculator!")

while True:  # Keep the system running until the teacher exits
    num_students = int(input("\nHow many students' grades do you want to enter? "))
    
    # Dictionary to store student names and grades
    student_grades = {}

    # 1️⃣ Use FOR loop to enter multiple student scores
    for i in range(num_students):
        name = input(f"\nEnter Student {i+1} Name: ")
        while True:  # Ensure valid score input
            try:
                score = int(input(f"Enter {name}'s Score (0-100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print("❌ Score must be between 0 and 100. Try again.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        # 2️⃣ Use IF conditions to assign grades
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        # Store student name and grade
        student_grades[name] = grade

    # 3️⃣ Display Final Grade Report
    print("\n🎓 Final Grade Report:")
    for student, grade in student_grades.items():
        print(f"📖 {student}: {grade}")

    # 4️⃣ Ask if the teacher wants to continue
    exit_choice = input("\nDo you want to enter more grades? (yes/no): ").lower()
    if exit_choice == "no":
        print("🏫 Thank you for using the Student Grade Calculator! Goodbye! 👋")
        break  # Exit the loop