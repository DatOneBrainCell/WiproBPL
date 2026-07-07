li1 = [1, 3, 5, 7]
li2 = [2, 4, 6, 8]

newLi = []

for i in range(len(li1)):
    newLi.insert(0, li1[i])
    newLi.insert(0, li2[i])

print(newLi)