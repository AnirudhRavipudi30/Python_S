# Define the file path
file_path = "/Users/anirudhravipudi/Desktop/Python_Scratch/TestLines.txt"

# Define the line positions
source_line_number = 50  # The line to remove
target_line_number = 96  # The line to insert at

# Read the existing file content into a list
with open(file_path, "r") as file:
    lines = file.readlines()

# Ensure the file has enough lines before attempting to move
if len(lines) >= max(source_line_number, target_line_number):
    # Remove text from line 50
    moved_text = lines.pop(source_line_number - 1).strip()  # Remove and strip newline

    # Insert it at line 96 (adjust for 0-based index)
    lines.insert(target_line_number - 1, moved_text + "\n")

    print(f"✅ Moved: '{moved_text}' from Line {source_line_number} to Line {target_line_number}")

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)

    print("\n✅ The file has been updated successfully!")

    # Display the updated file content
    print("\n📖 Updated File Content:\n")
    with open(file_path, "r") as file:
        print(file.read())

else:
    print(f"❌ The file has only {len(lines)} lines. Cannot move Line {source_line_number} to Line {target_line_number}.")