with open("Avengers.txt", 'r') as a:
    data = a.read()
    print(data)

# read() = reads the whole data
# read(l) = reads data of length l
# tell() = tells you about the position of file handle
# seek() = helps to reposition your file handle
# readlines() = reads data line by line

# Give each of these a try with the operations and print the results. 
# Remember to use 'r'