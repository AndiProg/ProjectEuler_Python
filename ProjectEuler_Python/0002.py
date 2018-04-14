temp = 0
n = 1
nMinusOne = 1
sumN = 0

while n < 4000000:

    temp = n + nMinusOne

    if temp % 2 == 0:
        sumN += temp

    nMinusOne = n
    n = temp

print(sumN)