# Write a  function to print the even numbers from a given list
# input = [1, 2, 4, 3, 5, 6]
# output = 2 4 6 

def even(li):
    # Iterate on the list li
    for i in li:
        # check for even elements
        if i % 2 == 0:
            print(i)
lst = [1, 2, 4, 3, 5, 6]
even(lst)

# Write a function that takes a list and returns a new list with unique elembers of the first list
# input = [1, 2, 3, 1, 2, 4]
# output = [1, 2, 3, 4]

lst1 = [1, 2, 3, 1, 2, 4]
def unique(li):
    new = []
    # iterate on the li list
    for i in li:
        # we are adding only unique elements in new list
        if i not in new:
            new.append(i)

    # return new list
    return new
unique(lst1)