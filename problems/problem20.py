def main():
    num = 1
    for i in range(100):
        num *= (i + 1)

    num = str(num)
    sum = 0

    for c in num:
        sum += int(c)

    return sum