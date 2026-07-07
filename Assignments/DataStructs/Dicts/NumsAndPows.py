dic = dict()

for i in range(1, 16):
    dic[i] = i**2

for keys, vals in dic.items():
    print(keys, ": ", vals)