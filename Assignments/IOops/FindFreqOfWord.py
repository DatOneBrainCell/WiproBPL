sWord = input("Enter a word:").lower()

with open("C:\\Users\\Admin\\Desktop\\23CS141\\txt\\SomethingAboutHistory.txt", "r") as tx:
    content = tx.read().lower()

words = content.split()

frequency = words.count(sWord)

print("Frequency of", sWord, "=", frequency)


'''O\P:
Enter a word:Napoleon 
Frequency of napoleon = 1
'''
