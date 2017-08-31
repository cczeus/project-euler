def main():
    max = 1000000
    sum = 0
    for i in range(1, max + 1):
        s = bin(i)[2:]
        if s == s[::-1] and str(i) == str(i)[::-1]:
            sum += i

    return sum
