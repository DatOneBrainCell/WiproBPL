def IsPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
if IsPrime(17):
    print("This is a prime number")
else:
    print("This is not a prime number")
    
'''O/P:
This is a prime number
'''
