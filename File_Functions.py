import os

# Provide the full file path
file_name = "/Users/anirudhravipudi/Desktop/Python_Scratch/Random.txt"  # Mac/Linux

# Ensure the directory exists before writing
os.makedirs(os.path.dirname(file_name), exist_ok=True)

# Writing to the file
with open(file_name, "w") as file:
    file.write("This is a test file stored in a specific directory.\n")
    file.write("File operations in Python are useful!\n")

print(f"Data written to '{file_name}' successfully!")

# Appending to the file
with open(file_name, "a") as file:
    file.write("Appending a new line to this file.\n")

print(f"Data appended to '{file_name}' successfully!")

# Reading from the file
print("\nReading from the file:")
with open(file_name, "r") as file:
    content = file.read()
    print(content)