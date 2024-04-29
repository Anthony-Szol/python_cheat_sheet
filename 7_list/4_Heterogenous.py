# With different datatypes
l = [3, "Szol", 9.9, False]

type(l)

type(l[2])

for i in l:
    print(l)

# 2-D Lists
l1 = [1,2,3]
l2 = [14, 8, 9]
l3 = [6, 99, 9]

m = [l1, l2, l3]

print(m)

# Indexing
# This will print l1
print(m[0])

# This will print l2
print(m[1])

# This will print l3
m[2]

# Iteration of 2-D List
for j in m:
    print(j)

# List all the numbers out of the []
for a in m:
    for b in a:
        print(b, end=" ")