def main():
    s = ""
    i = 0
    while len(s) < 1000001:
        i += 1
        s += str(i)

    s = list(s)

    n = 1
    for i in range(7):
        n *= int(s[(10 ** i) - 1])

    return n