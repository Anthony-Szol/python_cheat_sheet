# Dict has key value pair form of data
# Dict are ordered
# Does not support indexing
# Data can be accessed using key

# Creating an empty d
d = {}
print(type(d))

# Creating non empyt dict
food = {
    "Bagels" : 4,
    "Bananas" : 5,
    "Bread" : 7
}
print(food)

# Zip
name = ["Bagels", "Bananas", "Bread"]
price = [4, 5, 7]

food = dict(zip(name, price))
print(food)