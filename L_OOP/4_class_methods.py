# Apart from special methods you can make your custom methods
# Example: Humans can speak, greet, etc

class Human(): 
    # Constructor
    def __init__(self, name, age, hobby):
        # These are known as attributes of an object
        self.name = name
        self.age = age
        self.hobby = hobby
    # Methods
    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!!")

Anthony = Human("Anthony", 20, "Golfing")
Anthony.greet()

# More methods
class Human(): 
    # Constructor
    def __init__(self, name, age, hobby, alive = True):
        # These are known as attributes of an object
        self.name = name
        self.age = age
        self.hobby = hobby
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

h1 = Human("H1", 80)
h2 = Human("H2", 40)

Human.population    

h1.dead()
Human.population

h3 = Human("Adam", 26)
Human.population

h3.child(4)
Human.population