array = []

with open("problem18input.txt") as f:
    while True:
        c = f.readline()
        c = c.strip()
        if not c:
            break
        array.append(c.split(' '))

i = len(array) - 1
while i > 0:
    j = 0
    while j < len(array[i]) - 1:
        array[i - 1][j] = int(array[i - 1][j]) + int(max(array[i][j], array[i][j + 1]))
        j += 1
    i -= 1

print array