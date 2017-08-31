def isPentagonal(n):
    num = ((24 * float(n) + 1) ** .5 + 1) / 6
    return num == int(num)

def getPentagonal(n):
    return n * (3 * n - 1) / 2

def main():
    x = 2
    x1 = getPentagonal(x)
    y = 1
    y1 = getPentagonal(y)

    while not isPentagonal(x1 + y1) or not isPentagonal(x1 - y1):
        if y == 1:
            x += 1
            y = x - 1
            x1 = getPentagonal(x)
            y1 = getPentagonal(y)
        else:
            y -= 1
            y1 = getPentagonal(y)

    return x1 - y1