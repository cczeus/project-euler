import math

def getFactors(num):
    factors = []
    for j in range(2, int(math.sqrt(num)) + 1):
        if(num % j == 0):
            return False
    return True

def main():
    i = 3
    numPrimes = 1

    while numPrimes < 10001:
        if getFactors(i):
            numPrimes += 1
            if numPrimes == 10001:
                prime = i
        i += 2

    return prime