def main():
    max = 1000000
    primes = [True] * max
    primes[0] = False
    primes[1] = False

    for n in range(max):
        if primes[n]:
            for i in range(2 * n, max, n):
                primes[i] = False

    n = 10
    total = 0
    sum = 0
    while total < 11:
        n += 1
        sL = str(n)
        sR = str(n)
        while sL != "" and primes[int(sL)]:
            sL = list(sL)
            sL[len(sL) - 1] = ""
            sL = "".join(sL)

        while sR != "" and primes[int(sR)]:
            sR = list(sR)
            sR[0] = ""
            sR = "".join(sR)

        if sR == "" and sL == "":
            total += 1
            sum += n

    return sum