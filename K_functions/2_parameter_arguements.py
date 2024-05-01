# Parameters 
# These are place holders in the function
# When defining them we call them as parameters
# When passing the actual value we call them as arguements

def greet(name):
    print("Hi, how are you?", name)
greet("Anthony")

def add(a, b):
    c = a + b
    print(c)
add(2,3)

# Positional Arguments
# The value you pass when calling a function are matched according to their positions

def intro(name, hobby):
    print("Hey my name is", name)
    print("and my hobby is", hobby)
intro("Anthony", "golf")

# Default Arguments
# Giving default values to the parameters
# For these parameters passing value in arguments in optional

def intro(name, hobby = "golfing"):
    print("Hey my name is", name)
    print("and my hobby is", hobby)
intro("Anthony")

# You can override the default
intro("Tony Stark", "Avenging")

# Arbitrary Arguments
# When nuber of values you want to pass is not known
# Like we pass multiple values in print function
# The values are being stored in tuple

def test(*args):
    print(args)
test(1, 2, 3.4, "Tony Stark")

# Keyword Arguments
# Variable number of key word arguments
# It stores the data in the Dict format

def key( **kwargs ):
    #print(kwargs)
    #print(type(kwargs))
    for key1, values in kwargs.items():
        print(key1, values)
key(name = "Anthony", age = 20, hobbies = ["Golfing", "Swimming", "Reading"])

def mix(a, b, c, age = 25, *args, **kwargs):
    print(a, b, c)
    print(age)
    print(args)
    print(kwargs)
mix(2, 4, 5, 45, 6, 8, 9, name="Anthony", hobby="swimming")

