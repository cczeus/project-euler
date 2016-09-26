#DOESNT WORK, WILL INFINITELY LOOP, BUT WAS ABLE TO GET ANSWER FROM THIS

import math

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def isStillDivisible(num):
    for i in range(1, zeroTo):
        if num % i != 0:
            return False
    return True


def reduce():
    global num
    hasReduced = False
    for i in range(zeroTo, 1, -1):
        if num % i == 0 and isStillDivisible(num / i):
            num /= i
            hasReduced = True
    return hasReduced

def main():
    zeroTo = 20
    return 0
    num = factorial(zeroTo)
    while reduce():
        pass    
    return num