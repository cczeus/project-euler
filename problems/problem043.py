#3 Different methods
#Generating strings from end to beginning
#Generating strings from beginning to end
#Check all 0-9 pandigitals

def getPandigitalProducts(num):
    arr = []
    for i in range(num, 999, num):
        i = str(i)
        if int(i) < 100:
            i = '0' + i
        if len(i) == len(set(i)):
            if num == 11:
                if i[0] == '5':
                    arr.append(i)
            elif num == 7:
                if i[1] == '5':
                    arr.append(i)
            else:
                arr.append(i)
    return arr

def main():
    #Array of all pandigital products of a given number
    seventeen = getPandigitalProducts(17)
    thirteen = getPandigitalProducts(13)
    #Must start with 5
    eleven = getPandigitalProducts(11)
    #Second number must be 5
    seven = getPandigitalProducts(7)

    arr = []
    for i in seventeen:
        s = i
        for j in thirteen:
            if s[0] == j[1] and s[1] == j[2]:
                s = j[0] + s
                for k in eleven:
                    if s[0] == k[1] and s[1] == k[2]:
                        s = k[0] + s
                        for l in seven:
                            if s[0] == l[1] and s[1] == l[2]:
                                arr.append(l[0] + s)
                        s = s[1:]
                s = s[1:]

    #arr is now a list of potential last 6 digits
    print arr

    count = 0
    for i in arr:
        print ""
        print "Last 6 digits: " + str(i)
        digits = [j for j in range(0, 10)]
        for c in i:
            digits.remove(int(c))
        for d in digits:
            if d % 2 == 0:
                d4 = d
                newdigit = []
                for digit in digits:
                    newdigit.append(digit)
                newdigit.remove(d)
                for d3 in newdigit:
                    if (d3 + int(s[0]) + d4) % 3 == 0:
                        if d3 == newdigit[0]:
                            n1 = int( str(newdigit[1]) + str(newdigit[2]) + str(d3) + str(d4) + i )
                            n2 = int( str(newdigit[2]) + str(newdigit[1]) + str(d3) + str(d4) + i )
                        elif d3 == newdigit[1]:
                            n1 = int( str(newdigit[0]) + str(newdigit[2]) + str(d3) + str(d4) + i )
                            n2 = int( str(newdigit[2]) + str(newdigit[0]) + str(d3) + str(d4) + i )
                        else:
                            n1 = int( str(newdigit[1]) + str(newdigit[0]) + str(d3) + str(d4) + i )
                            n2 = int( str(newdigit[0]) + str(newdigit[1]) + str(d3) + str(d4) + i )
                        print n1
                        print n2
                        count += n1
                        count += n2
                newdigit.append(d4)

    return count

            