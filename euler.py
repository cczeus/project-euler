from problems import *
import datetime

problems = {
    '1': [problem001, 233168],
    '2': [problem002, 4613732],
    '3': [problem003, 6857],
    '4': [problem004, 906609],
    '5': [problem005, 232792560],
    '6': [problem006, 25164150],
    '7': [problem007, 104743],
    '8': [problem008, 23514624000],
    '9': [problem009, 31875000],
    '10': [problem010, 142913828922],
    '11': [problem011, 70600674],
    '12': [problem012, 76576500],
    '13': [problem013, 5537376230],
    '14': [problem014, 837799],
    '15': [problem015, 137846528820],
    '16': [problem016, 1366],
    '17': [problem017, 21124],
    '18': [problem018, 1074],
    '19': [problem019, 171],
    '20': [problem020, 648],
    '21': [problem021, 31626],
    '22': [problem022, 871198282],
    '23': [problem023, 4179871],
    '24': [problem024, 2783915460],
    '25': [problem025, 4782],
    '26': [problem026, 983],
    '27': [problem027, -59231],
    '28': [problem028, 669171001],
    '29': [problem029, 9183],
    '30': [problem030, 443839],
    '31': [problem031, 73682],
    '32': [problem032, 45228],
    '33': [problem033, 100],
    '34': [problem034, 40730],
    '35': [problem035, 55],
    '36': [problem036, 872187],
    '37': [problem037, 748317]
}

def testAll():
    num = 0
    totalTime = 0
    failures = []

    for k, v in problems.items():
        start = datetime.datetime.now()
        ans = v[0].main()
        stop = datetime.datetime.now()
        diff = stop - start
        totalTime += int(diff.total_seconds() * 1000)
        num += 1
        if ans != v[1]:
            failures.append([k, str(ans), str(v[1])])

    for i in failures:
        print "FAILED: Problem " + i[0] + ", got " + i[1] + ", expected " + i[2]
    
    if len(failures) > 0:
        print ""

    print "=====Summary====="
    print "Successes: " + str(num - len(failures))
    print "Failures: " + str(len(failures))
    print "Total Time Elapsed: " + str(totalTime) + "ms"


def testProblem(num):
    problem = problems[num]
    start = datetime.datetime.now()
    answer = problem[0].main()
    stop = datetime.datetime.now()
    diff = stop - start
    if answer == problem[1]:
        print "Success. Answer: " + str(problem[1])
    elif problem[1] == 0:
        print "Problem" + num + ": " + str(answer)
    else:
        print "Failure. Your answer was " + str(answer) + " while the correct answer is " + str(problem[1])
    print "Solved in " + str(int(diff.total_seconds() * 1000)) + "ms"

def main():
    problemNum = raw_input("Problem #")
    print ""
    print ""
    if problemNum == "all":
        testAll()
    elif int(problemNum) > 0 and int(problemNum) <= len(problems):
        testProblem(problemNum)
    else:
        print "Choose either a problem number, 1-" + str(len(problems)) + " or \'all\'"
        main()
    print ""
    print ""

main()
