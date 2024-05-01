# Print all vowels of a given string
text = "Harry Potter is better than Lord of the Rings"

for i in text:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i)

# Write a sentence inputting 3 strings
animal = input("Please enter animal")
pet = input("please enter animal name")
toy = input("Please enter a toy")

print("My {}'s name is {} and their favorite toy is a {}".format(animal,pet,toy))