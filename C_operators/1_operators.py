# Express is a operand (x and y) with an operator (+,-,*,/)

# Arithmetic Operators
# These are used for arithmetic operators
# Addition
a = 1
b = 2
print(a + b)

# Subtraction
c = 3
d = 1
print(c-d)

# Multiply
e = 10
f = 2
print(e*f)

# Divide will always yield float value
g = 5
h = 5
print(g/h)

# You can add strings as well (String concatenation)
first = 'Anthony'
last = 'Szol'
print(first + last)

# Modulus %: will give remainder
print(a,b)
print(a%b)

# In floor division //, the result is floored to the nearest smaller int
i=2.3
j=1
print(i//j)

# To the power accepts two values base and power **
print(2**3)

# Comparison operators can be used to compare values in mathematical terms
# == (True if equal)
k=2
l=8
print(k==l)
#Result will return false

print(l==8)
# Result will return true

# != (True if not equal)
print(k!=l)
# Result will return true

# < (Less than) and > (Greater than)
print(k<l)
print(k>l)

# <= (Less than or equal to) and >= (Greater than or equal to)
k<=l
k>=l
# Note: You don't always need to use print function

# Assignment Operators are used to assign values to variables. 
# The most common assignment operator is =, which simply assigns 
# the value on the right to the variable on the left
# Assigning a value to a variable
m = 10
print("Initial m:", m)

# Adding a value using +=
m += 5
print("After m += 5:", m)

# Multiplying a value using *=
m *= 2
print("After m *= 2:", m)

# Subtracting a value using -=
m -= 4
print("After m -= 4:", m)

# Dividing a value using /=
m /= 3
print("After m /= 3:", m)

# Logical Operators (and, or, not): used to combine conditional
# statements, allowing you to evaluate whether conditions are 
# True or False

# and
n = 5
o = 7
print(n > 0 and o > 0)  
# Both conditions are true, so this prints True.

# or
print(n > 0 or o > 0)  
# One condition is true (b > 0), so this prints True.

# not
p = False
print(not p)  
# p is False, so 'not a' is True.

# Special Operators
# in operators tells you if an object is part of other object or not
name = 'Anthony'
print('Ant' in name)
 # Result is true

print('Tony' in name)
# Result is false

# is
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)    
# False, because they are different objects with the same values

print(a is c)    
# True, because they are the same object

print(a is not b) 
# True
