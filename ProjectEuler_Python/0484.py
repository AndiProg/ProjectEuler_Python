from sympy.ntheory import factorint

#print(factorint(10**15))
def gcdKK(k):
    list = factorint(k)
    for p_i, n_i in list.items():
        if n_i % p_i != 0:
            k //= p_i
    return k

summe = 0
for i in range(2,10**5+1):
    summe += gcdKK(i)
print(summe)


