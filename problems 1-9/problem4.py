numDigits = 3

def isPalindrome(num1, num2):
    n = str(num1 * num2)
    return str(n) == str(n)[::-1]

max = 10 ** numDigits - 1
palNum = 0
palNum1 = 0
palNum2 = 0
for i in range(max, 0, -1):
    for j in range(i, 0, -1):
        if(isPalindrome(i, j) and i * j > palNum):
            palNum = i * j
            palNum1 = i
            palNum2 = j

print palNum