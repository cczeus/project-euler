from problems import *
import datetime

problems = {
    '1': [problem1, 233168],
    '2': [problem2, 4613732],
    '3': [problem3, 6857],
    '4': [problem4, 906609],
    '5': [problem5, 232792560],
    '6': [problem6, 25164150],
    '7': [problem7, 104743],
    '8': [problem8, 23514624000],
    '9': [problem9, 31875000]
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
