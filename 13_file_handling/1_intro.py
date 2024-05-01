# Make sure to download Avengers.txt and Star Wars.json files for this section
#A file is a container in a computer system for storing data
# Data is permanently stored

# Types of Data are text or binary

# Opening a file
# Open: returns a file handle
# In order to perform any kind of operations on file first we open it

a = open("avengers.txt")
type(a)

a.read()

a.close()