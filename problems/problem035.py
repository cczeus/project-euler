def permutate(str):
    s = str
    arr = []
    while s not in arr:
        arr.append(s)
        s = list(s)
        s.append(s[0])
        s[0] = ""
        s = "".join(s)
    return arr

def main():
    max = 1000000
    primes = [True] * max
    primes[0] = False
    primes[1] = False

    for n in range(max):
        if primes[n]:
            for i in range(2 * n, max, n):
                primes[i] = False
        if "0" in str(n):
            primes[n] = False

    for n in range(max):
        if primes[n]:
            arr = permutate(str(n))
            allPrime = True
            for a in arr:
                if not primes[int(a)]:
                    allPrime = False
                    break

            if not allPrime:
                for a in arr:
                    primes[int(a)] = False


    sum = 0
    for n in range(max):
        if primes[n]:
            sum += 1

    return sum