import math
import lib

def isAmicable(num, factors):
    return factors[num] < 10000 and num == factors[factors[num]] and num != factors[num]

def main():
    factors = []
    for i in range(10000):
        factors.append(lib.getFactorsSum(i))

    sum = 0
    for i in range(10000):
        if isAmicable(i, factors):
            sum += factors[i]

    return sum