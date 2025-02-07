# Define the file path
file_path = "/Users/anirudhravipudi/Desktop/Python_Scratch/FileFunctionsExample.txt"

# 1️⃣ Read and print existing file content
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("📖 Existing File Content:\n")
        print(content)
except FileNotFoundError:
    print(f"❌ File not found at: {file_path}")
    exit()

# 2️⃣ Append new car details to the file
new_content = """Car: Mercedes AMG GT
Price: $150,000
Color: Silver
"""

with open(file_path, "a") as file:
    file.write(new_content)

print("\n✅ New data appended successfully!")

# 3️⃣ Read and print updated file content
with open(file_path, "r") as file:
    updated_content = file.read()

print("\n📖 Updated File Content:\n")
print(updated_content)