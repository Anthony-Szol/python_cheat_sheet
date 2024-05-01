# Scope of a variable
# There are two scope of a variable: Global and Local
# Global variable can be used anywhere in a program
# Local variable can only be used locally inside a program(function)

# a can be used anywhere in the program
a = 5

def func():
    print(a)

func()
print(a)

def func():
    x = 3
    print(x)

func()
print(a)
print(x)


def func():
    global a
    a = 20
    print(a)

print(a)
func()
print(a)