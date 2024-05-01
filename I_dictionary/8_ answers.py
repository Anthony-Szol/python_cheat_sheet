# Find the freqcuency (freq = {}) of each name in the school attendance

attendance = ("Matt","Kate", "Tim", "Kate", "Tony", "Jake", "Tim", "Steve", "Randy", "Kim", "Carly", "Kate")

freq = {}
for i in attendance:
    # Check for presence
    if i not in freq:
        freq[i] = 1
    # if present increment the freq by factor of 1
    else:
        freq[i] += 1
print(freq)