s = input("Enter a string: ")
n = int(input("Enter an integer n: "))

if n > 0:
    lastN = s[-n:]
else:
    lastN = ""

print(lastN * n)

'''O/P:
Enter a string: Wipro
Enter an integer n: 3
propropro
'''
