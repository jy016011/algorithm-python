from functools import cmp_to_key

'''
프로그래머스 코딩테스트 고득점 kit 정렬, 문제 2번: 가장 큰 수
'''


def comparator(s1, s2):
    temp1 = s1 + s2
    temp2 = s2 + s1
    return (int(temp1) > int(temp2)) - (int(temp1) < int(temp2))


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(comparator), reverse=True)

    return str(int("".join(numbers)))


print(solution([6, 10, 2]) == "6210")
print(solution([3, 30, 34, 5, 9]) == "9534330")
print(solution([979, 97, 978, 81, 818, 817]) == "9799797881881817")
print(solution([0, 0, 0]) == "0")
