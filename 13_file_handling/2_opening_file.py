# Modes of opening a file
# 'r' read only
# 'w' write only
# 'a' appending data at the end of file
# 'wt' write text
# 'wb' write binary
# 'rb' read binary
# 'rt; read text

a = open("Avengers.txt", "w")
a.write("Avengers assumble")
a.close()

# With Open
# Most common way to perform operation on files
# It closes the file after performing operations
with open("Avengers.txt") as a:
    print(a.read())