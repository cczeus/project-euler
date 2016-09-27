import math

def main():
    sum = 0
    with open("problems/input/problem13.txt") as f:
        while True:
            c = f.readline()
            if not c:
                break
            sum += int(c)

    while math.log10(sum) > 10:
        sum /= 10

    return sum