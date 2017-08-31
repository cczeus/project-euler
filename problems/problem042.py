def main():
    triangle_nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    with open("problems/input/problem042.txt") as f:
        while True:
            c = f.readline()
            c = c.strip().replace("\"", "").lower()
            if not c:
                break
            array = c.split(',')

    count = 0
    for word in array:
        score = 0
        for char in word:
            score += alphabet.index(char) + 1
        if score in triangle_nums:
            count += 1
        if score > 210:
            print score

    return count