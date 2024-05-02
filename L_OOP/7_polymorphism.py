# Havinh many forms
# Same class method can work differently for different objects

# Operator level polymorphism

a = 2
b = 3

# Adding
a + b

# Concatn
"2" + "2"

3 - 2

"Anthony" * 2

# Functional Level Polymorphisms
# len
# sum 
# custom

l = [1, 2, 3, 4]
len(l)

sum(l)

def mul(*args):
    total = 1
    for i in arges:
        total *= i
    
    return total

mul(2, 3, 4)

class Human:
    def speak(self, language):
        print("I speak", language)

h1 = Human()
h2 = Human()

h1.speak("English")