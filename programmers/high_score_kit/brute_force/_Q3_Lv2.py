import math
from itertools import permutations


def solution(numbers):
    answer = 0
    data = list(map(str, numbers))
    candidate = set()
    for i in range(1, len(numbers) + 1):
        permute = list(permutations(data, i))
        permute = set(list(map(lambda x: int(''.join(x)), permute)))
        candidate = candidate.union(permute)

    for number in candidate:
        if number <= 1:
            continue
        if isPrime(number):
            answer += 1
    return answer


def isPrime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


print(solution("011"))
