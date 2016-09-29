import math
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 1000000

def getDigit(i):
    global num
    global digits
    coeff = math.factorial(i)
    for n in range(len(digits)):
        if (n + 1) * coeff >= num:
            if n != 0:
                num -= (n) * coeff
            digit = digits[n]
            digits.remove(digit)
            return digit

def main():
    dig = ""
    for i in range(9, -1, -1):
        dig += str(getDigit(i))
    return int(dig)