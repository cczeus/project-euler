def getLen(num, nums):
    if str(num) in nums:
        return nums[str(num)]
    elif num % 2 == 0:
        leng = getLen(num / 2, nums) + 1
        nums[str(num)] = leng
        return leng
    else:
        leng = getLen((3 * num) + 1, nums) + 1
        nums[str(num)] = leng
        return leng

def main():
    nums = {'1': 1}

    for startNum in range(1, 1000000):
        if str(startNum) not in nums:
            nums[str(startNum)] = getLen(startNum, nums)

    max = 0
    num = 0
    for k, v in nums.items():
        if v > max:
            max = v
            num = int(k)

    return num