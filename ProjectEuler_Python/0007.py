import math

def isPrime(n):
    if n < 2:
        return False;
    
    if n == 2:
        return True;
    
    for divisor in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False

    return True

n = 0
primeCounter = 0

while True:
    if isPrime(n):
        primeCounter += 1
        if primeCounter == 10001:
            break
    n += 1

print(n)