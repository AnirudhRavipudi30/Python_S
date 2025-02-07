# 📌 Creating Sets
bmw_models = {"M3", "M5", "M8", "X5 M", "X7 M60i"}  # Changed X7 M to X7 M60i
audi_models = {"RS5", "RS7", "R8", "Q8", "M5"}

# 1️⃣ Adding Elements to a Set
bmw_models.add("M4")
print("🔹 BMW Models after adding M4:", bmw_models)

# 2️⃣ Removing an Element from a Set
bmw_models.remove("X7 M60i")  # Removes X7 M60i
print("🔹 BMW Models after removing X7 M60i:", bmw_models)

# 3️⃣ Union (All Unique Elements from Both Sets)
all_models = bmw_models.union(audi_models)
print("🔹 Union (All Car Models):", all_models)

# 4️⃣ Intersection (Common Elements)
common_models = bmw_models.intersection(audi_models)
print("🔹 Common Models (BMW & Audi):", common_models)

# 5️⃣ Difference (BMW Models NOT in Audi)
bmw_unique = bmw_models.difference(audi_models)
print("🔹 BMW Models NOT in Audi:", bmw_unique)

# 6️⃣ Symmetric Difference (Elements in One Set, But Not Both)
unique_cars = bmw_models.symmetric_difference(audi_models)
print("🔹 Cars in One Set but Not Both:", unique_cars)

# 7️⃣ Checking if One Set is a Subset of Another
print("🔹 Is {'M5', 'M3'} a subset of BMW Models?", {"M5", "M3"}.issubset(bmw_models))

# 8️⃣ Checking if One Set is a Superset of Another
print("🔹 Is BMW Models a superset of {'M3', 'M5'}?", bmw_models.issuperset({"M3", "M5"}))

# 9️⃣ Checking if Two Sets are Disjoint (No Common Elements)
print("🔹 Are BMW and Audi sets disjoint?", bmw_models.isdisjoint(audi_models))