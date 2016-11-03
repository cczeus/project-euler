def factorial(num):
    if num <= 1:
        return 1
    else:
        return factorial(num - 1) * num

def main():
    fact = [factorial(i) for i in range(10)]
    max = factorial(9)
    max *= len(str(max))

    s = 0
    for i in range(10, max + 1):
        sum = 0
        for c in str(i):
            sum += fact[int(c)]
        if sum == i:
            s += i

    return s