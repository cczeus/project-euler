import math

def getFactors(num):
    factors = []
    i = 1
    while i <= math.sqrt(num):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)
        i += 1
    return factors

sum = 1
n = 2
while len(getFactors(sum)) <= 500:
    sum += n
    n += 1

print sum