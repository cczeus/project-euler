import math

def isStillDivisible(num):
    for i in range(2, 21):
        if num % i != 0:
            return False
    return True

def main():
    factors = []
    num = 1
    for i in range(2, 21):
        factors.append(i)
        num *= i

    for i in range(20, 2, -1):
        if isStillDivisible(num / i):
            num /= i

    return num