import sys

def CalculateHappiness():
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    string3 = sys.argv[3]
    
    likedNumbers = string1.split("-")
    dislikedNumbers = string2.split("-")
    myNumbers = string3.split("-")
    
    currentHappiness = 0
    
    for num in myNumbers:
        if num in likedNumbers:
            currentHappiness = currentHappiness + 1
        elif num in dislikedNumbers:
            currentHappiness = currentHappiness - 1
            
    print(currentHappiness)

CalculateHappiness()

'''O/P:
$ python Happiness.py 3-1 5-7 1-5-3-8
1
'''
