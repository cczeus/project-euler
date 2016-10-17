import lib

def main():
    max = 0
    product = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            maxCount = 0
            while(lib.isPrime(n ** 2 + a * n + b)):
                n += 1
                maxCount += 1

            if maxCount > max:
                print str(a) + " " + str(b) + " " + str(maxCount)
                max = maxCount
                product = a * b

    return product