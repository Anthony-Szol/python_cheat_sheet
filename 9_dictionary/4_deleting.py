# pop
# popitem
# del

food = {
    "Bagels" : 4,
    "Bananas" : 5,
    "Bread" : 7
}

food["Bread"] = {"Sourdough":7, "Wheat": 5}
print(food)

food["Milk"] = 10
print(food)

new = {"Candy Bar" : 2, "Pasta" : 6, "Dog Food" : 35}
food.update(new)
print(food)

# dict.pop(key) 
food.pop("Bananas")
print(food)

# dict.popitem() will delete the last item
food.popitem()
print(food)

# del object will delete dict from the memory
del food
print(food)