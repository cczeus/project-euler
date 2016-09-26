def fibonacci(num1, num2):
    if num2 < 4000000:
        num1 += num2
        if num1 % 2 == 0:
            return num1 + fibonacci(num2, num1)
        else:
            return fibonacci(num2, num1)
    else:
        return 0

def main():
    return fibonacci(1, 1)