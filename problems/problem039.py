def main():
    count = [0] * 1001
    maxB = 0
    for a in range(1, 292):
        for b in range(a, 500):
            c = (a ** 2 + b ** 2) ** 0.5
            if c + a + b > 1000:
                break
            if b > maxB:
                maxB = b
            if int(c) == c:
                count[int(c + a + b)] += 1
    maxLength = 0
    maxNum = 0
    for i in range(len(count)):
        if count[i] > maxLength:
            maxNum = i
            maxLength = count[i]
    return maxNum