def FindEven(l):
    newLi = []
    for el in l:
        if el % 2 == 0:
            newLi.append(el)
            
    return newLi
    
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(FindEven(l))

'''O/P:
[2, 4, 6, 8]
'''
