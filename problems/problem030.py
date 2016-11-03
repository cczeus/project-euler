def main():
    sum = 0

    for i in range(2, 5 * 9 ** 5):
        s = 0
        for c in str(i):
            s += int(c) ** 5

        if s == i:
            sum += i

    return sum