try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a/b)

except(ZeroDivisionError):
    print("You cant divide by zero")


'''O\P:
Enter a number: 4
Enter another number: 0
You cant divide by zero
'''
