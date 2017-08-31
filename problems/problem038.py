def main():
    #Number must be larger than 918273645
    #Number can't be double digit, as you wouldn't get the proper number of digits
    #Number can't be triple digit
    max = 0
    for i in range(9182, 9876):
        s = str(i) + str(i * 2)
        if int(s) > max and "".join(sorted(s)) == "123456789":
            max = int(s)
    return max
