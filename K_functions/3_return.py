# Return
# A function call ends when return statement is executed
# It returns the expression back to the function
# The code after return statement are not executed
# If there is no return value then function returns None

# Return vs Print
def add(a, b):
    c = a + b
    print(c)
add(2,3)

a = add(2,3)

print(a, type(a))


def add(a, b):
    c = a + b
    return(c)
b = add(2,3)
print(b, type(b))

# Returning multiple values
def intro(name, age, hobby):
    return name, age, hobby
a, b, c = intro("Anthony", 20, "Golf")
print(a, b, c)

d = intro("Anthony", 20, "Golf")
print(d)
