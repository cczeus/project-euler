import math

def getFactorsSum(num):
    sum = 1
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            sum += i
            sum += num / i
            if i == num / i:
                sum -= i
        i += 1
    return sum

def isAbundant(num):
    return getFactorsSum(num) > num

def isSumOfAbundant(num):
    for i in range(1, (num + 1) / 2):
        if abundant[i] and abundant[num - i]:
            return True
    return False

"""
abundant = []
for i in range(28123):
    abundant.append(isAbundant(i))


sum = 0
for i in range(28124):
    print i
    if not isSumOfAbundant(i):
        sum += i
"""
print getFactorsSum(28)