food = {
    "Bagels" : 4,
    "Bananas" : 5,
    "Bread" : 7
}

for i in food:
    print(i)

# How to print the cooresponing values
for u in food:
    print(u, food[u])


# using dict.items()
for key, value in food.items():
    print(key, value)