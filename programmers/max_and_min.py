import sys


def solution(s):
    number_strings = s.split(" ")
    minNumber = sys.maxsize
    maxNumber = -sys.maxsize
    for number in number_strings:
        minNumber = min(minNumber, int(number))
        maxNumber = max(maxNumber, int(number))
    return str(minNumber) + " " +str(maxNumber)

print(solution("1 2 3 4"))