import re

st = ['789', '123', '004']

for s in st:
    if re.fullmatch('[0-7]+', s):
        print(s, ": Octal")
    else:
        print(s, ": Not Octal")

'''O/P:
789 : Not Octal
123 : Octal
004 : Octal
'''
