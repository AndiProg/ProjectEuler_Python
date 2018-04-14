import math

def getPrimeFactors(n):
    
    divided = True
    primeFactors = []
    
    while divided:
        
        divided = False
        
        for divisor in range(2, math.ceil(math.sqrt(n))):
            if n % divisor == 0:
                primeFactors.append(divisor)
                n /= divisor
                divided = True
                break

    primeFactors.append(int(n))
    
    return primeFactors

print(max(getPrimeFactors(600851475143)))