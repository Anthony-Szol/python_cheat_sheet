# You can write both text and binary file
# You can either write or append in a file

# Create a new file
with open("new.txt", 'w') as a:
    a.write("This is a new file")

# Write in existing
with open("Avengers.txt", 'w') as a:
    # \n is for new line
    a.write("This is an existing file \n")
    a.write("This is a new line")

a.close()
