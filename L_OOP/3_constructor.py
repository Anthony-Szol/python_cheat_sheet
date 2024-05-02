# A constructor is a special method used to create and initialize an object of a class
# This method is defied in the class
# THey are executed automatically at the time of object creation

class Human(): 
    # I want some properties to be with every human object
    # Dunder _
    
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

Anthony = Human("Anthony", 20, "Golfing")
print(Anthony)