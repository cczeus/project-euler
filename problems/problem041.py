def main():
    max = 10 ** 7
    primes = [True] * max
    primes[0] = False
    primes[1] = False
    for i in range(4, max, 2):
        primes[i] = False

    for i in range(3, max, 2):
        if primes[i]:
            for j in range(2 * i, max, i):
                primes[j] = False

    print "Primes array created"
    for i in range(max - 1, 0, -1):
        if primes[i] and "".join(sorted(list(str(i)))) == "1234567":
            return i
    return 1