def main():
    num = 2 ** 1000
    sum = 0

    i = 1
    while 10 ** i < num * 10:
        n = ((num % (10 ** i)) - (num % (10 ** (i - 1)))) / (10 ** (i - 1))
        sum += n
        i += 1

    sum = 0
    num = str(num)
    for i in range(len(num)):
        sum += int(num[i])

    return sum