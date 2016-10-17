import math

def isPrime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    elif num < 0:
        return False

    for j in range(3, int(math.sqrt(num)) + 1, 2):
        if(num % j == 0):
            return False
    return True

def getFactors(num):
    factors = []
    i = 1
    while i <= math.sqrt(num):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)
        i += 1
    return factors

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