import math
import lib

def new():
    max = 100000000
    primes = [1] * max
    n = 2
    while primes[n] <= 500:
        if primes[n] == 1:
            for i in range(n, max / n):
                primes[n * i] += 1




def main():
    sum = 1
    n = 2
    while len(lib.getFactors(sum)) <= 500:
        sum += n
        n += 1
    return sum