import math
import lib

def main():
    i = 3
    numPrimes = 1

    while numPrimes < 10001:
        if lib.isPrime(i):
            numPrimes += 1
            if numPrimes == 10001:
                prime = i
        i += 2

    return prime