try:
    num = int(input("Enter a number:"))
    isPrime = True
    if num <= 1:
        isPrime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                isPrime = False
                break
                
    if isPrime:
        print("Prime")
    else:
        print("Not Prime")
except ValueError:
    print("Invalid input")
    
'''O\P:
Enter a number:hi
Invalid input
'''
