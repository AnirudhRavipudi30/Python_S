# Ask the user to input a mathematical expression
expression = input("Enter a mathematical expression (e.g., 5 + 3 * 2): ")

try:
    # Evaluate the expression safely
    result = eval(expression)
    print(f"\nThe result of '{expression}' is: {result}")
except Exception as e:
    print(f"\nError: Invalid expression! ({e})")