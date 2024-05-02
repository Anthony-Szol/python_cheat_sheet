# These are common to the class
# Example: Population of Human class is comon to all objects

class Human(): 
    # Class Variables
    population = 0

    # Constructor
    def __init__(self, name, age, hobby):
        # These are known as attributes of an object
        self.name = name
        self.age = age
        self.hobby = hobby

        # Increment population for every new human object
        Human.population += 1

    # Methods
    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!!")

Anthony = Human("Anthony", 20, "Golfing")
Human.population

Ironman = Human("Ironman", 40, "Flying")
Human.population