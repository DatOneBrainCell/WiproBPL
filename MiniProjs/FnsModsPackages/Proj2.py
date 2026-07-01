def IsPalindrome(name):
    if name == name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def CountTheVowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in name:
        if ch in vowels:
            count = count + 1
    return count

def FrequencyOfLetters(name):
    freqMap = {}
    uniqueCharsLi = []
    for ch in name:
        if ch != " ":
            if ch not in freqMap:
                freqMap[ch] = 1
                uniqueCharsLi.append(ch)
            else:
                freqMap[ch] = freqMap[ch] + 1
    
    pairLi = []
    for ch in uniqueCharsLi:
        pairLi.append(ch + "-" + str(freqMap[ch]))
    
    resStr = ", ".join(pairLi)
    return resStr

userInput = input("Enter a string: ")

palindromeResult = IsPalindrome(userInput)
vowelCount = CountTheVowels(userInput)
letterFreq = FrequencyOfLetters(userInput)

print(palindromeResult)
print("No of vowels: ", vowelCount)
print("Frequency of letters: ", letterFreq)

'''O/P:
Enter a string: MALAYALAM
Yes it is a palindrome.
No of vowels:  4
Frequency of letters:  M-2, A-4, L-2, Y-1
'''
