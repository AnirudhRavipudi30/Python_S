file_path = "/Users/anirudhravipudi/Desktop/Python_Scratch/TestLines.txt"

# Define the line number to be removed (e.g., 30th line)
remove_line_number = 30  

# Read the existing file content into a list
with open(file_path, "r") as file:
    lines = file.readlines()

# Ensure the file has enough lines before attempting to remove
if len(lines) >= remove_line_number:
    removed_line = lines.pop(remove_line_number - 1)  # Remove line at index (30-1 = 29)
    print(f"✅ Removed Line {remove_line_number}: {removed_line.strip()}")
else:
    print(f"❌ The file has only {len(lines)} lines. Cannot remove line {remove_line_number}.")

# Write the updated content back to the file
with open(file_path, "w") as file:
    file.writelines(lines)

print("✅ The file has been updated successfully!")
