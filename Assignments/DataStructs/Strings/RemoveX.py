s = input("Enter a string: ")
ls = s.split()
if ls[0] == 'x' or ls[0] == 'X':
    ls.remove(ls[0])
if ls[-1] == 'x' or ls[-1] == 'X':
    ls.remove(ls[-1])

ns = ('').join(ls)
print(ns)