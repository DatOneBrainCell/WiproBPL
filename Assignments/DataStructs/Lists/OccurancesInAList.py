li = [1, 2, 4, 2, 1, 4, 1, 4]

print(li)

newLi = []
dic = dict()

for l in li:
    if l not in newLi:
        dic[l] = 1
        newLi.append(l)
    else:
        dic[l] += 1

num = int(input("Enter a number: "))
if num in dic.keys():
    print("Occrances: ", dic[num])
else:
    print("Enter a valid Number")