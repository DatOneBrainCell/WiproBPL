dic = {1: 20, 2: 54, 3: "string", 4: 4.55}

addn = 0

for vals in dic.values():
    if isinstance(vals, int):
        addn += vals

print(addn)