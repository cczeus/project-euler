import math

def isPrime(num):
    factors = []
    for j in range(2, int(math.sqrt(num)) + 1):
        if(num % j == 0):
            return False
    return True

sum = 2

i = 3
while i < 2000000:
    if isPrime(i):
        sum += i
    i += 2

print sum