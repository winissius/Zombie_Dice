VetA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
VetB = []
for pos, n in enumerate(VetA):
    if pos % 2 == 0:
        VetB.append(VetA[pos] * 2)
    else:
        VetB.append(VetA[pos]**2)
print(VetA)
print(VetB)
