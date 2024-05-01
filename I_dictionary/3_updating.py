# Using key
# Update method

food = {
    "Bagels" : 4,
    "Bananas" : 5,
    "Bread" : 7
}

# Updating the existing value
food["Bread"] = {"Sourdough":7, "Wheat": 5}
print(food)

# Updating with new value
food["Milk"] = 10
print(food)

# Update
new = {"Candy Bar" : 2, "Pasta" : 6, "Dog Food" : 35}
food.update(new)
print(food)