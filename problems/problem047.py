max = 175
hasFourDistinctPrimeFactors = [False] * (max ** 4)

def main():
    primes = [True] * max
    primes[0] = False
    primes[1] = False

    for n in range(max):
        if primes[n]:
            for i in range(2 * n, max, n):
                primes[i] = False

    for f1 in range(max):
        if primes[f1]:
            for f2 in range(f1 + 1, max):
                if primes[f2]:
                    for f3 in range(f2 + 1, max):
                        if primes[f3]:
                            for f4 in range(f3 + 1, max):
                                if primes[f4]:
                                    addFactors(f1, f2, f3, f4)

    inARow = 0
    for i in range(max ** 4):
        if hasFourDistinctPrimeFactors[i]:
            inARow = inARow + 1
        else :
            inARow = 0

        if inARow == 4:
            return i - 3

def addFactors(f1, f2, f3, f4):
    product = f1 * f2 * f3 * f4
    hasFourDistinctPrimeFactors[product] = True
    for i in range(f1 * product, max, f1):
        hasFourDistinctPrimeFactors[i] = True

    for i in range(f2 * product, max, f2):
        hasFourDistinctPrimeFactors[i] = True

    for i in range(f3 * product, max, f3):
        hasFourDistinctPrimeFactors[i] = True

    for i in range(f4 * product, max, f4):
        hasFourDistinctPrimeFactors[i] = True