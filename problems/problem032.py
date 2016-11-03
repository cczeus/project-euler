def isPandigital(num1):
    chars = []
    for c in str(num1):
        if c in chars:
            return False
        else:
            chars.append(c)
    return True

def arePandigital(num1, num2):
    if not isPandigital(num1) or not isPandigital(num2):
        return False
    for c in str(num1):
        if c in str(num2):
            return False
    return True

def main():
    products = []
    for i in range(9876):
        if isPandigital(i) and "0" not in str(i):
            for j in range(9876):
                if i * j > 20000:
                    break
                elif isPandigital(j) and "0" not in str(j) and "0" not in str(i * j):
                    if arePandigital(i, j) and arePandigital(i, i * j) and arePandigital(j, i * j):
                        if (len(str(i)) + len(str(j)) + len(str(i * j)) == 9):
                            if i * j not in products:
                                products.append(i * j)
    sum = 0
    for n in products:
        sum += n

    i = 39
    j = 186
    return sum

