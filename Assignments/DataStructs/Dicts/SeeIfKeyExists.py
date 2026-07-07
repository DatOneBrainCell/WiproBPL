dic = {1: 10, 2: 20, 3: 30}
print(dic)

ip = int(input("Enter a key: "))

if ip in dic.keys():
    print("It exists")
else:
    print("It doesnt exist")