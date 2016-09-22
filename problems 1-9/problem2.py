def fibonacci(num1, num2):
    global sum
    if num2 < 4000000:
        num1 += num2
        if num1 % 2 == 0:
            sum += num1
        fibonacci(num2, num1)

sum = 2
fibonacci(1, 2)
print sum