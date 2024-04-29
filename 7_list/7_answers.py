# Given a list of population sensus, you need to find the total population
# Each element in the list represents total members in a family

population = [4, 6, 5, 8, 9, 3, 2, 4, 5, 4, 3, 2, 3, 4]

# Start with a baseline variable
total_population = 0
# Sum the poulation list up
for i in population:
    total_population += i
print(total_population)