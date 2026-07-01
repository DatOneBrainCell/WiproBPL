def ColorSort(colors):
    li = list(colors.split('-'))
    li.sort()
    newSt = '-'.join(li)
    return newSt
    
ip = input("Enter a string of colors: ")
print(ColorSort(ip))

'''O/P:
Enter a string of colors: green-yellow-red-orange
green-orange-red-yellow
'''
