dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

newDict = dict()

for keys, vals in dict1.items():
    newDict[keys] = vals

for keys, vals in dict2.items():
    newDict[keys] = vals

for keys, vals in dict3.items():
    newDict[keys] = vals

print(newDict)