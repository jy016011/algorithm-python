import math


def solution(brown, red):
    answer = []
    total_tile = brown + red
    divisor = []
    for i in range(3, int(math.sqrt(total_tile)) + 1):
        if total_tile % i == 0:
            divisor.append([total_tile // i, i])
    for width, height in divisor:
        if (width - 2) * (height - 2) == red:
            answer = [width, height]
            break

    return answer


print(solution(10, 2) == [4, 3])
print(solution(8, 1) == [3, 3])
print(solution(24, 24) == [8, 6])
