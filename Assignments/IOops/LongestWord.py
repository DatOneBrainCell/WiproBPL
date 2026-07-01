with open("C:\\Users\\Admin\\Desktop\\23CS141\\txt\\SomethingAboutHistory.txt", "r") as tx:
    text = tx.read()

words = text.split()

longest = max(words, key=len)

print("Longest word: ", longest)

'''O\P:
Longest word:  Carthegenian
'''
