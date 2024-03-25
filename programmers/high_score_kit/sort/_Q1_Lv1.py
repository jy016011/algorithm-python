'''
프로그래머스 코딩테스트 고득점 kit 정렬, 문제 1번: K번째 수
'''


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i - 1:j])[k - 1])

    return answer


# answer: [5, 6, 3]
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
