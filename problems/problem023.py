import math
import lib

def isAbundant(num):
    return lib.getFactorsSum(num) > num

def isSumOfAbundant(num, abundant):
    for i in range(1, (num + 2) / 2):
        if abundant[i] and abundant[num - i]:
            return True
    return False

def main():
    abundant = []
    for i in range(28123):
        abundant.append(isAbundant(i))

    sum = 0
    for i in range(1, 28124):
        if not isSumOfAbundant(i, abundant):
            sum += i

    return sum