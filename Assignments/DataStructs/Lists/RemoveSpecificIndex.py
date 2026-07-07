li = [1, 2, 3, 4, 5, 6]
print(li)

ip = int(input("Enter a number: "))

if ip < len(li):
    li.pop(ip)
    print(li)
else:
    print("Index out of range")