n = int(input("Enter the no of lines: "))
li = []

with open("C:\\Users\\Admin\\Desktop\\23CS141\\txt\\SomethingAboutHistory.txt", "r") as tx:
    for lines in tx:
        li.append(lines)
    
    for i in range(n):
        print(li[i])

'''O\P:
Enter the no of lines: 2
Napoleon Bonaparte was a French general
Hannibal Barca was a Carthegenian general
'''
