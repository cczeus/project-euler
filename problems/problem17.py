def main():
    """1-9"""
    oneThroughNine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4

    """10-19"""
    tenThroughTwenty = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
 
    """20-99"""
    twentyThroughNinetyNine = (8 * oneThroughNine) + (10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6))

    """100-999"""
    oneHundredThroughNHNN = (100 * oneThroughNine) + (900 * 7) + (99 * 9 * 3) + ((oneThroughNine + tenThroughTwenty + twentyThroughNinetyNine) * 9)

    """1000"""
    oneThousand = 11

    sum = oneThroughNine + tenThroughTwenty + twentyThroughNinetyNine + oneHundredThroughNHNN + oneThousand
    return sum
