import math

def main():
    
    max = 0
    maxIndex = 0
    for i in range(2, 1000):
        remainders = [False] * i
        n = 0
        num = 1
        while remainders[num] == False:
            remainders[num] = True
            num *= 10
            num %= i
            n += 1
        if n > max:
            max = n
            maxIndex = i

    return maxIndex