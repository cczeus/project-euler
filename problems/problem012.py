import math
import lib

def main():
    sum = 1
    n = 2
    while len(lib.getFactors(sum)) <= 500:
        sum += n
        n += 1
    return sum