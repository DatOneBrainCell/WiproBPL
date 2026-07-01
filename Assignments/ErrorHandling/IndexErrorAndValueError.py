li = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]
try:
    val = li[int(input("Enter a number: "))]
    if val > 0:
        print("Positive")
    elif val < 0:
        print("Negative")
    else:
        print("Zero")
except (IndexError, ValueError):
    print("Invalid index or input")
    
'''O\P:
Enter a number: 45
Invalid index or input
'''
