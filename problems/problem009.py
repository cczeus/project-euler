def isPythagoreanTriple(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    return nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2

def main():
    for a in range(1, 999):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if isPythagoreanTriple(a, b, c):
                return a * b * c