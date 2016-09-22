import math

factors = []

def getFactorsSum(num):
    sum = 1
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            sum += i
            sum += num / i
        i += 1
    return sum

def isAmicable(num):
    return factors[num] < 10000 and num == factors[factors[num]] and num != factors[num]

for i in range(10000):
    factors.append(getFactorsSum(i))

sum = 0
for i in range(10000):
    if isAmicable(i):
        sum += factors[i]

print sum