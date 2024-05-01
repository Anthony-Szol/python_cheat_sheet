# These are mainly used when we need nameless functions for a short period of time

def add(a, b):
    return a + b
add(3, 4)

(lambda a, b : a + b)(3, 4)

func = lambda a, b : a + b

func(5, 4)

def larger(a, b):
    if a > b:
        return a
    else:
        return b

(lambda a, b : a if a > b else b)(43, 5)

large = lambda a, b : a if a > b else b
large(62, 7)

lst = [(12, 56), (2, 4), (12, 56)]

def k(f):
    return f[1]
lst.sort(key = k)

lst.sort(key = lambda x : [1])
 