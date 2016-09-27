import math
import lib

def main():
    num = 600851475143
    factors = lib.getFactors(num)
    maxPrimeFactor = 1
    for factor in factors:
        if len(lib.getFactors(factor)) == 2 and factor > maxPrimeFactor:
            maxPrimeFactor = factor;

    return maxPrimeFactor