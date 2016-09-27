import math

def isAbundant(num):
    return lib.getFactorsSum(num) > num

def isSumOfAbundant(num):
    for i in range(1, (num + 1) / 2):
        if abundant[i] and abundant[num - i]:
            return True
    return False

def main():
    return 1
"""
abundant = []
for i in range(28123):
    abundant.append(isAbundant(i))


sum = 0
for i in range(28124):
    print i
    if not isSumOfAbundant(i):
        sum += i
"""