def main():

    max = 2000000

    max += 1
    prime = [True] * (max)
    prime[0] = False
    prime[1] = False
    prime[2] = True

    for i in range(4, max, 2):
        prime[i] = False

    for i in range(3, max, 2):
        if prime[i]:
            for j in range(2 * i, max, i):
                prime[j] = False

    sum = 0
    i = -1
    while i < len(prime):
        if prime[i]:
            sum += i
        i += 1

    return sum


    """
    sum = 2

    i = 3
    while i < 2000000:
        if lib.isPrime(i):
            sum += i
        i += 2

    return sum"""