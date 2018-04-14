def CheckAbundant(n):
    divisorSum = 0
    for divisor in range(1,n):
        if n % divisor == 0:
            divisorSum += divisor
    if divisorSum > n:
        return 1
    else:
        return 0

listAbundantNumbers = []

#for i in range(1,28124):
#    if CheckAbundant(i):
#        listAbundantNumbers.append(i)
#        print(i)
#NumberFile = open('AbundantNumbers.txt','w')
#for item in listAbundantNumbers:
#    NumberFile.write('%s\n' % item)
#NumberFile.close


listAbundantNumbers = [int(line.rstrip('\n')) for line in open('AbundantNumbers.txt')]

print(listAbundantNumbers)

