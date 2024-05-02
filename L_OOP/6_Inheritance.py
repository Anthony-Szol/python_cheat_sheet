# When a class dervices every attributes and methods from other class
# It gets access to all its methods and attributes
# This helps in resuability of code

class Human(): 
    # Constructor
    def __init__(self, name, age, hobby, alive = True):
        # These are known as attributes of an object
        self.name = name
        self.age = age
        self.hobby = hobby

        Human.population += 1
        Human.data.append(self.name)
        
    # Methods
    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!!")
    
    def dead(self):
        if self.alive:
            print(self.name, "is no longer alive")
            Human.poulation -=1
            self.alive = False
        else:
            print("This person is already dead")

    def child(self, number):
        Human.population += number

Anthony = Human("Anthony", 20, "Golfing")
Ironman = Human("Emma", 20, "Flying")
Human.population

# Inheritance
# Human is base class 
# Employee is derived class
class employee(Human):
    # Reinitiate constructor
    def __init__(self, name, age, hobby, company, post):
        super().__init__(name, age, hobby)

        # attributes for employee class
        self.company = company 
        self.post = post

e1 = employee("Jarvis", 40, "Working")
Human.population

Human.data