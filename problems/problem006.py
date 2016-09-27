def main():
    sumOfSquares = 0
    squareOfSums = 0
    for i in range(101):
        sumOfSquares += i * i
        squareOfSums += i

    squareOfSums **= 2
    return squareOfSums - sumOfSquares