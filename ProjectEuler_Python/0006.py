sumN = 0
sumOfSquares = 0

for n in range(1, 101):
    sumN += n
    sumOfSquares += n**2

squareOfSum = sumN**2

print(squareOfSum - sumOfSquares)