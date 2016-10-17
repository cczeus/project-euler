def main():
    num = 1
    prev = 0
    index = 1
    while len(str(num)) < 1000:
        temp = num
        num += prev
        prev = temp
        index += 1

    return index