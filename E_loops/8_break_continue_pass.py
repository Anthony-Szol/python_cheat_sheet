# These statements are used to ater the flow of a program
# Break: breaks the form of program once this condition is hit
# Continue: It skips that particular iteration
# Pass: Avoids syntax error

# pass
for i in range(1,10):
    pass

# continue
for i in range(1,10):
    if i == 5:
        continue
    print(i)

# break
for i in range(1,10):
    if i == 5:
        break
    print(i, end=" ")