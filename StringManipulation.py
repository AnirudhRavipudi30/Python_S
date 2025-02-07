# 📌 Sample String
text = "   The BMW M5 CS is the most powerful M5 ever made.   "

# 1️⃣ Convert to Uppercase & Lowercase
print("🔹 Uppercase:", text.upper())
print("🔹 Lowercase:", text.lower())

# 2️⃣ Remove Leading & Trailing Spaces
trimmed_text = text.strip()
print("🔹 Trimmed String:", trimmed_text)

# 3️⃣ Find & Replace a Word
new_text = text.replace("M5", "M8")
print("🔹 Replaced String:", new_text)

# 4️⃣ Split String into Words
words = trimmed_text.split()
print("🔹 Split Words:", words)

# 5️⃣ Join Words Back into a Sentence
joined_text = " - ".join(words)
print("🔹 Joined String:", joined_text)

# 6️⃣ Find Substring Position
position = trimmed_text.find("M5")
print("🔹 Position of 'M5':", position)

# 7️⃣ Count Occurrences of a Word
count_m5 = trimmed_text.count("M5")
print("🔹 Count of 'M5':", count_m5)

# 8️⃣ Check if String is Alphabetic, Numeric, or Alphanumeric
print("🔹 Is Alphabetic?:", trimmed_text.isalpha())  # False (due to spaces & numbers)
print("🔹 Is Numeric?:", trimmed_text.isdigit())  # False (contains text)
print("🔹 Is Alphanumeric?:", "BMWM5CS".isalnum())  # True

# 9️⃣ Reverse the String
reversed_text = trimmed_text[::-1]
print("🔹 Reversed String:", reversed_text)

# 🔟 Check if String Starts or Ends with a Certain Word
print("🔹 Starts with 'The'?", trimmed_text.startswith("The"))
print("🔹 Ends with 'made.'?", trimmed_text.endswith("made."))