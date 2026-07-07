tup = (1, 2, 3, 4, 5, 6, 7, 8)
print(tup)

ip = int(input("Enter a integer: "))

if ip in tup:
    print("It is present in the tuple")
else:
    print("It is not present in the tuple")

'''O/P 1:
(1, 2, 3, 4, 5, 6, 7, 8)
Enter a integer: 10
It is not present in the tuple

O/P 2:
(1, 2, 3, 4, 5, 6, 7, 8)
Enter a integer: 4
It is present in the tuple
'''