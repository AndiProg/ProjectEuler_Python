def d(n):
    divisorSum = 0
    for divisor in range(1,n):
        if n % divisor == 0:
            divisorSum += divisor
    return divisorSum

def CheckAmicable(a):
    b = d(a)
    if d(b) == a and a != b:
        return 1
    return 0

amicableSum = 0
for i in range(1,10000):
    print(i)
    if CheckAmicable(i):
        amicableSum += i
        
print(amicableSum)
# 31626