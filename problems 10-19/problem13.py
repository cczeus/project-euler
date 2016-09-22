import math

sum = 0

with open("problem13input.txt") as f:
    while True:
        c = f.readline()
        if not c:
            break
        sum += int(c)

print sum

while math.log10(sum) > 10:
    sum /= 10

print sum