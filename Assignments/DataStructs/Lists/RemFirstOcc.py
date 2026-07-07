li = [1, 2, 1, 3, 2, 5, 1, 3, 6, 2]
print(li)

ip = int(input("Enter the number to deleted: "))

if ip in li:
    li.remove(ip)
else:
    print("Index out of range")

print(li)