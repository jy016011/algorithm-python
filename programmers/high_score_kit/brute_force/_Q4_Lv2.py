import math

'''
프로그래머스 코딩테스트 고득점 kit 완전탐색, 문제 4번: 카펫
'''


def solution(brown, yellow):
    total_area = brown + yellow
    combinations = []
    cnt = 1
    for row in range(1, int(math.sqrt(total_area)) + 1):
        if total_area % row == 0:
            col = total_area // row
            combinations.append([col, row])

    answer = []
    for col, row in combinations:
        if (col * 2) + (row - 2) * 2 == brown:
            return [col, row]

    return answer


print(solution(10, 2) == [4, 3])
print(solution(8, 1) == [3, 3])
print(solution(24, 24) == [8, 6])
