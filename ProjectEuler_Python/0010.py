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

sumOfPrimes = 0

for index in range(1, 2000000):
    if isPrime(index):
        sumOfPrimes += index

print(sumOfPrimes)