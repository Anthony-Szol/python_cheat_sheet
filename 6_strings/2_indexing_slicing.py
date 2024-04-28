# The length of the string is indexing
# Starting at 0, each character is counted to determine the length

name = "Anthony Szol"

# You can select one charater
print(name[11])

# You can print multiple characters (name[start,end])
print(name[7:12])

# Remember, the end will be cut off. If you the end of the string include, your end must be plus 1. 

# You can index backwards. The start will be -1
print(name[-1])

# This will give whole string
print(name[:])