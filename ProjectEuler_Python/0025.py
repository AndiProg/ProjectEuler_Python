fk1 = 1
fk2 = 1
fLen = 0
index = 2
while fLen < 1000:
    tmp = fk2 + fk1
    fk1 = fk2
    fk2 = tmp 
    index += 1
    fLen = len(str(tmp))
print(index)

