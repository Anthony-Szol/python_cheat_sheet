# Try: This block handles the error in you code if any of it exists
# Except: This block gives the output that you want to show if your code is faulty
a = 5
b = 0
c = 2

try:
    print(a/b)
except:
    pass
    print("There is an error that you might want to look at")

print("Avada Kedavra!")

# Now see what happens when the try works
try:
    print(a/c)
except:
    pass
    print("There is an error that you might want to look at")

print("Avada Kedavra!")


# Finally