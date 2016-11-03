def main():
    t = 200
    t += 1
    sum = 0
    for i in range(0, t, 200):
        for j in range(0, t - i, 100):
            for k in range(0, t - i - j, 50):
                for l in range(0, t - i - j - k, 20):
                    for m in range(0, t - i - j - k - l, 10):
                        for n in range(0, t - i - j - k - l - m, 5):
                            for o in range(0, t - i - j - k - l - m - n, 2):
                                sum += 1

    return sum