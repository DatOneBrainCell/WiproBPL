with open("C:\\Users\\Admin\\Desktop\\23CS141\\txt\\SomethingAboutHistory.txt", "r") as tx:
    lines = tx.readlines()

lines = [line.strip() for line in lines]

print("Contents in list:")
print(lines)

'''O\P:
Contents in list:
['Napoleon Bonaparte was a French general', 'Hannibal Barca was a Carthegenian general', 'Alexander the Great was a Roman general', 'who got stabbed 26 times, I think, I forgot']
'''
