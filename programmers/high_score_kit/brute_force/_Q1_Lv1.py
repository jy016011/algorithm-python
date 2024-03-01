'''
프로그래머스 코딩테스트 고득점 kit 완전탐색, 문제 1번: 최소직사각형
'''


def solution(sizes):
    max_vals = []
    min_vals = []
    for size in sizes:
        max_vals.append(max(size))
        min_vals.append(min(size))

    return max(max_vals) * max(min_vals)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133)
