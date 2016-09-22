array = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

def getSum(string):
    sum = 0
    for c in string:
        sum += alphabet.index(c) + 1
    return sum

#Reads the input into an array
with open("problem22input.txt") as f:
    while True:
        c = f.readline()
        c = c.strip()
        if not c:
            break
        array = c.split(',')

#Formats the array into proper lowercase strings
for i in range(len(array)):
    array[i] = array[i][1:len(array[i]) - 1].lower()

array.sort()

sum = 0
for i in range(len(array)):
    sum += getSum(array[i]) * (i + 1)

print sum
