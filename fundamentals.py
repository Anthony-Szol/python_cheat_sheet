#The purpose of this file is to understand the fundamentals of Python.


# Want to show something as output: Use print function

print("Hello World")

# You will find the result as Hello World. Test the function by
#changing the words to Howdy Partner

# Variables must start with a letter or the underscore charater
# Variables cannot start with numbers or be a function word (ie. and, or, for)
# Variables are case-sensitive

x = 5
y_2=6
print(x + y_2)

# Results will come back 11.

# Data Types in Python
#Thoughout this section, I will use the function (type) to display the type of data

# Integers are whole numers from -infinity to infinity. These do not have decimal points.

number = 24
print(type(number))

# Floats are numbers with decimal points

f = 1.24
print(type(f))

# Booleans are data types that are True or False

b1 = True
print(type(b1))

b2 = False
print(type(b2))

# Strings are anything you can type. 
# Strings must be contained in quotes ("") or ('')

s1 = 'Anthony knows Python!!!'
print(s1)
print(type(s1))

# If you use a word such as don't , you must use double quotes ("")
# or else Python will come back with an error. Example below:

# s2 = 'don't'
# print(s2)

# None is like NULL in other coding languages. No value. 

n = None
print(n)
print(type(n))

# Input function  is used to receive user input as a string value. 
# When you use this function, Python will pause your program and wait for the user 
# to type something into the console and press enter. The text entered by the user is 
# then returned as a string and can be stored in a variable for further use.

# Ask the user for their name
name = input("Please enter your name: ")

# Print a greeting that includes the entered name
print("Hello, " + name + "!")


i = input("Type 5.1:")
print(i)
print(type(i))

# As you notice in the results, the input function created 5.1 into a string.
# We can convert it with a Type conversion
# This will convert the 5.1 string into a float

i2 = float(i)
print(i2)
print(type(i2))