def CountNameOccurrences(txtSt):
    occr = txtSt.count("Alex")
    return occr

ip = input("Enter your name: ")
res = CountNameOccurrences(ip)

print("Occurances: ", res)

'''O/P:
Enter your name: Alexa, how many times is Alex in this program, take a guess, Alex
Occurances:  3
'''
