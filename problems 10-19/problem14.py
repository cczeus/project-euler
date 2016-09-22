maxLength = 1
maxNum = 1
for startNum in range(1, 1000000):
    i = startNum
    length = 1
    while i > 1:
        length += 1
        if i % 2 == 0:
            i /= 2
        else :
            i = (3 * i) + 1
    if length > maxLength:
        maxLength = length
        maxNum = startNum

print maxNum