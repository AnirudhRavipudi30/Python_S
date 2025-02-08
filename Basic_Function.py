# This is a basic Function call
def basictest():
    Basic_Math = 63 * 96/30;
    return Basic_Math;
print(basictest());

# This is a basic function call with parameters
def Greet(name):
    print(f"Hello {name}, How are you? ");
Greet("Anirudh");

# Using return to send a value back from a function
def Multiply(a, b):
    return a * b;
print("Multiplication of the 2 numbers: ", Multiply(63, 96));

# If no argument is provided the function uses a default value
def Greet_name(name="Anirudh"):
    print(f"Hello, {name}!")
Greet_name("Stephen");
Greet_name();

#Keyword Arguments are used to pass amed arguments which can be used to pass the values in any order
def Car_Details(Make, Model, Year):
    print(f"Car : {Make}, {Model}, {Year}, Would you like to know the price?");
Car_Details(Make = "BMW", Model = "540i", Year = 2020);
Car_Details(Year = 2021, Model = "S7", Make = "Audi");
Car_Details(Make = "Mercedes", Year = 2023, Model = "AMG GT 4-Door");

#Lambda Function
Car_Depreciation = lambda Price, Year: Price * 0.10 * (2025 - Year);
print("Depreciation of the car: ", Car_Depreciation(63000, 2019));
