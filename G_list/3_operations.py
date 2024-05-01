# List inbuilt methods
budget = [100, 200, 150, 100]

# Count: Returns the count of an object
budget.count(100)

# Index: Returns the index of 1st occurance of an object
budget.index(100)

# Pop: Remove and returns the last element of a list
drop = budget.pop()
# Confirm element is removed
print(budget)

# Remove
name = ["Loki", "Ironman", "Captain America", "Hulk"]
name.remove("Ironman")

# Confirm element is removed
print(name)

# Sort: It sorts our list
name.sort()
print(name)

# Insert: Helps to add an element at a given index .insert(index, element)
name.insert(4, "Thor")
print(name)

# Append: 
name.append("Black Widow")
print(name)

# Look what happens when you append a list to an existing list
young_avengers = ["Ms Marvel", "Kid Loki", "Kate Bishop"]
name.append(young_avengers)
print(name)
# The addition remains in the [] and will be counted as a single index

# Extend: Will expand the appended list into seperate index
name.extend(young_avengers)
print(name)
