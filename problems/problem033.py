import math

def reduce(num, den):
    for n in range(2, int(math.sqrt(num)) + 2):
        if num % n == 0 and den % n == 0:
            num /= n
            den /= n
            return reduce(num, den)
    return den

def main():
    n1 = 1
    d1 = 1
    for i in range(1, 10):
        for j in range(1, 10):
            if j == i: continue
            for k in range(1, 10):
                if (10 * i + j) * k == (10 * k + i) * j:
                    n1 *= k
                    d1 *= j
    return reduce(n1, d1)