from math import gcd
from math import lcm

"""
You are given a positive integer n. You have to find 4 positive integers a,b,c,d

such that

    a+b+c+d=n
and
    gcd(a,b)=lcm(c,d)

If there are several possible answers you can output any of them. It is possible to show that the answer always exists.

In this problem gcd(a,b)
denotes the greatest common divisor of a and b, and lcm(c,d) denotes the least common multiple of c and d

Input

The input consists of multiple test cases. The first line contains a single integer t
(1≤t≤104) — the number of test cases. Description of the test cases follows.

Each test case contains a single line with integer n
(4≤n≤109) — the sum of a, b, c, and d

Output

For each test case output 4
positive integers a, b, c, d such that a+b+c+d=n and gcd(a,b)=lcm(c,d).
"""


def divideInt(problems):
    toPrint = []
    for i in range(problems):
        num = int(input())
        # Getting our number as 4 integer parts
        result = ([num // 4 + (1 if x < num % 4 else 0) for x in range(4)])
        # getting equal gcd and lcm from the array of numbers.
        solution = gcdAndLcm(result)
        toPrint.append(solution)
    # print(toPrint)
    # Printing the solutions after calculaStions
    for i in toPrint:
        for j in i:
            print(j, end=" ")
        print()



def gcdAndLcm(numbers):
    # print(numbers)
    foundSolution = False
    gcdNum = 0
    lcmNum = 0
    while foundSolution == False:
        gcdNum = gcd(numbers[0], numbers[1])
        lcmNum = lcm(numbers[2], numbers[3])
        if gcdNum != lcmNum:
            # If gcd is too small, bring a number from right to left.
            if gcdNum > lcmNum:
                if numbers[2] != 1 and numbers[3] != 1:
                    # If position 2 in the array is 1
                    if numbers[2] != 1:
                        numbers[2] -= 1
                        numbers[0] += 1
                        gcdNum = gcd(numbers[0], numbers[1])
                        lcmNum = lcm(numbers[2], numbers[3])
                        if gcdNum == lcmNum:
                            # print(gcdNum, lcmNum, numbers)
                            break
                    if numbers[3] != 1:
                        numbers[3] -= 1
                        numbers[0] += 1
                        # Check the gcd again.
                        gcdNum = gcd(numbers[0], numbers[1])
                        lcmNum = lcm(numbers[2], numbers[3])
                        if gcdNum == lcmNum:
                            # print(gcdNum, lcmNum, numbers)
                            break
            elif lcmNum > gcdNum:
                if numbers[2] != 1 and numbers[3] != 1:
                    # If position 2 in the array is 1
                    if numbers[2] != 1:
                        numbers[2] -= 1
                        numbers[0] += 1
                        gcdNum = gcd(numbers[0], numbers[1])
                        lcmNum = lcm(numbers[2], numbers[3])
                        if gcdNum == lcmNum:
                            # Leave instantly.
                            # print(gcdNum, lcmNum, numbers)
                            break
                    if numbers[3] != 1:
                        numbers[3] -= 1
                        numbers[0] += 1
                        # Check the gcd again.
                        gcdNum = gcd(numbers[0], numbers[1])
                        lcmNum = lcm(numbers[2], numbers[3])
                        if gcdNum == lcmNum:
                            # print(gcdNum, lcmNum, numbers)
                            break
        else:
            foundSolution = True
    # saving the solution
    return [int(numbers[0]),int(numbers[1]),int(numbers[2]),int(numbers[3])]

def main():
    numberOfProblems = int(input())
    divideInt(numberOfProblems)

if __name__ == "__main__":
    main()
