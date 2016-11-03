def isPalindromic(s):
    s = list(s)
    for i in range((len(s) + 1) / 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def main():
    max = 1000000
    sum = 0
    for i in range(1, max + 1):
        s = bin(i)[2:]
        if isPalindromic(str(s)) and isPalindromic(str(i)):
            sum += i

    return sum
