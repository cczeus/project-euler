"""DOESNT WORK, WILL INFINITELY LOOP, BUT WAS ABLE TO GET ANSWER FROM THIS"""

import math

zeroTo = 20

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def isStillDivisible(num):
    for i in range(1, zeroTo):
        if num % i != 0:
            return False
    return True

num = factorial(zeroTo)

def reduce():
    global num
    hasReduced = False
    for i in range(zeroTo, 1, -1):
        if num % i == 0 and isStillDivisible(num / i):
            num /= i
            hasReduced = True
    return hasReduced

while reduce():
    pass    
print num

