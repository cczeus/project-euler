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

def main():
    num = 600851475143
    factors = getFactors(num)
    maxPrimeFactor = 1
    for factor in factors:
        if len(getFactors(factor)) == 2 and factor > maxPrimeFactor:
            maxPrimeFactor = factor;

    return maxPrimeFactor