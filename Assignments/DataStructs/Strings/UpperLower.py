s = "Vlad the Impaler was a Valacian noble who lived around Romania"

upperCount = 0
lowerCount = 0

for ch in s:
    if ch.isupper():
        upperCount += 1
    elif ch.islower():
        lowerCount += 1

print("Uppercase letters: ", upperCount, "\nLowercase letters: ", lowerCount)

'''O/P:
Uppercase letters:  4
Lowercase letters:  48
'''