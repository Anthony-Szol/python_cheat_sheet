# This mode helps us to append in a file

with open("Avengers.txt", "w") as a:
    a.write("Avengers Assumble!!!\n")

with open("Avengers.txt", "a") as b:
    b.write("Ironman\n")
    b.write("Captain America\n")
    b.write("Black Widow\n")
    b.write("Hawkeye\n")
    b.write("Hulk\n")
    b.write("Thor")
