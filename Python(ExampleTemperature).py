def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("🌡️ Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"🌡️ {celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"🌡️ {fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
else:
    print("❌ Invalid choice. Please enter 1 or 2.")
