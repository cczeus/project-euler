import math

def main():
    for i in range(144, 100000):
        n = i * (2 * i - 1)

        if isTriangular(n) and isPentagonal(n):
            return n

def isTriangular(num):
    a = .5
    b = .5
    c = -num
    ans1 = -b + math.sqrt(b ** 2 - (4 * a * c)) / (2 * a)
    ans2 = -b - math.sqrt(b ** 2 - (4 * a * c)) / (2 * a)

    return (ans1 > 0 and ans1 % 1 == 0) or (ans2 > 0 and ans2 % 1 == 0)

def isPentagonal(num):
    a = 1.5
    b = -.5
    c = -num
    ans1 = (-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    ans2 = (-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)

    return (ans1 > 0 and ans1 % 1 == 0) or (ans2 > 0 and ans2 % 1 == 0)