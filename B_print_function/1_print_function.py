# Printing multiple values using print function
# Recap: below is a single print
print('Anthony')

# The result will come out as Anthony. Now you can print 
# multiple items at once. 
print('Anthony', 'Harry Potter', 'Golf', 11.4, 14, 27)

# Notice strings are in the quoations while intergers and floats are not. 

# sep function can be used to create a seperation in the multiple print
# This sep=',' seperates by comma
print('Anthony', 'Harry Potter', 'Golf', 11.4, 14, 27, sep=',')

# This sep='\n' seperates by lines
print('Anthony', 'Harry Potter', 'Golf', 11.4, 14, 27, sep='\n')

# This can seperate with an arrow
print('Anthony','Iron Man', sep='=>')

# Changing default vaule of seperator
# Typically this print function will print on seperate lines
print('Anthony is')
print('Iron Man')

# The end function will let you change the print function to be on the same row
print('Anthony is', end=' ')
print('Iron Man')

# The function changes the default and allows the print to be on the same line. 
# You can include comma or arrows as well in the end function. 