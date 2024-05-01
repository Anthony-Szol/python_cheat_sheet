# Data Structure 
# A data structure is a specialized format for organizing, processing, retrieving and storing data
# There are various methods: List, Dictionary, Sets, Tuples

 # Lists
# Ordered collection of data
# Lists are mutable type of data structure
# It can contain multiple type of data
# Lists are changeable
# Lists are iterable

# Creating a list
l1 = list()
print(type(l1))

l2 = [1, 3, 5, 2]
type(l2)

len(l2)

# Accessing
l2

l2[0]

# Mutability or change

l2[0] = 7


# Iterable
for i in l2:
    print(i)
