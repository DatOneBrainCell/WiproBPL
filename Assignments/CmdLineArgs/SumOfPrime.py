import sys

primeSum = 0

for arg in sys.argv[1:]:
    num = int(arg)
    
    if num > 1:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        
        if isPrime:
            primeSum = primeSum + num

print(primeSum)

'''O/P:
$ python SumOfPrime.py 1 2 3 4 5 6 7 8 9 10
17
'''
