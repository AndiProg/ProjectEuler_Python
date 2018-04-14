def isPalindrome(n):
    
    n = str(n)
    last = len(n) - 1
    
    for index in range(0, int(len(n) / 2)):
        if(n[index] != n[last - index]):
            return False
        
    return True

maxPalindrome = -1

for n1 in range(999, 99, -1):
    for n2 in range(999, 99, -1):
        n3 = n1 * n2
        if isPalindrome(n3):
            if n3 > maxPalindrome:
                maxPalindrome = n3

print(maxPalindrome)