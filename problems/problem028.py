def main():
    #Generate a 2D array with the spiral values
    n = 2
    l = 1001
    array = []
    for i in range(l):
        a1 = []
        for j in range(l):
            a1.append(1)
        array.append(a1)
    x = (l - 1) / 2 - 1
    y = (l - 1) / 2 + 1
    for layer in range((l - 1) / 2):
        for i in range(2 * (layer + 1)):
            x += 1
            array[x][y] = n
            n += 1
        for i in range(2 * (layer + 1)):
            y -= 1
            array[x][y] = n
            n += 1
        for i in range(2 * (layer + 1)):
            x -= 1
            array[x][y] = n
            n += 1
        for i in range(2 * (layer + 1)):
            y += 1
            array[x][y] = n
            n += 1
        x -= 1
        y += 1

    sum = 0
    for i in range(l):
        sum += array[l-1-i][i]
        sum += array[i][i]
    sum -= array[(l-1)/2][(l-1)/2]
    return sum