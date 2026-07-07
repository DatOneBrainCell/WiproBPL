dic = {1914: "WW1", 1939: "WW2", 1066: "Battle of Hastings", 1200: "Crusades"}

print("Keys:")
for keys in dic.keys():
    print(keys, end = ', ')
print()

print("Values:")
for vals in dic.values():
    print(vals, end = ', ')
print()

print("Keys:")
for keys, vals in dic.items():
    print(keys, "and", vals, end = ', ')
print()
