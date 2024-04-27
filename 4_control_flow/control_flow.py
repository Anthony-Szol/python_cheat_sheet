# Control Flow Statements
# If statements - "If" the conditions are meant, the results will show the expressions (True)
# Else statements - Anything "else" besides the IF statements, the results will show another expression (False)

# Syntax of If/Else
age = int(input())
# Use if else
if age >= 18: 
   # Example of a nestled (Where you can put a syntax of if/else within a syntax): Check if age is > 75
   if age > 75:
        print("Not safe to drive")
   else:
        print("You can drive!")
    # You can print multiple lines
        print("Be careful")
else:
    print("Cannot Drive")

# The elif condition is used to include multiple conditional expressions after the "if" condition. 
num = int(input())

if num > 0:
        print("Positive")
elif num == 0:
        print("Zero")
else:
      print("Negative")

# Find MAX in list
marks = [90, 30, 100, 50, 80, 95]
max(marks)

# MIN in list
min(marks)




