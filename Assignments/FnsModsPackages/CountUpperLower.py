def UpperLower(s):
    upperCount = 0
    lowerCount = 0
    
    for ch in s:
        if ch.isupper():
            upperCount += 1
        elif ch.islower():
            lowerCount += 1
            
    print(upperCount)
    print(lowerCount)
    
s = "Napoleon Bonaparte was a renouned French General"
UpperLower(s)

'''O/P:
4
38
'''
