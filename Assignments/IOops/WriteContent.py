text = input("Write something: ")

with open("C:\\Users\\Admin\\Desktop\\23CS141\\txt\\SomethingAboutHistory.txt", "a") as tx:
    tx.write(text + "\n")

print("Data appended successfully.")

'''O\P:
Write something:  who got stabbed 26 times, I think, I forgot
Data appended successfully.
'''

'''Text file:
Napoleon Bonaparte was a French general
Hannibal Barca was a Carthegenian general
Alexander the Great was a Roman general
 who got stabbed 26 times, I think, I forgot
'''
