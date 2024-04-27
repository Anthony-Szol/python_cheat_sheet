# Write a control flow for a school grading system. Grading system is as followed:
# A = 90+
# B = 80-89
# C = 70-79
# D = 60-69
# F = < 60

grade = int(input())
if grade >= 90:
    print("A")
elif grade >= 80 and grade <90:
    print("B")
elif grade >= 70 and grade <80:
    print("C")
elif grade >= 60 and grade <70:
    print("D")
else:
    print("F")