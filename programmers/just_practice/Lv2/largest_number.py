from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(comparator), reverse=True)
    return str(int(''.join(numbers)))


def comparator(o1, o2):
    s1 = o1 + o2
    s2 = o2 + o1
    return (int(s1) > int(s2)) - (int(s1) < int(s2))


print(solution([6, 10, 2]) == '6210')
print(solution([3, 30, 34, 5, 9]) == '9534330')
print(solution([0, 0, 0]) == '0')
