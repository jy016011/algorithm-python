from itertools import permutations

'''
프로그래머스 코딩테스트 고득점 kit 완전탐색, 문제 5번: 피로도
'''


def solution(k, dungeons):
    answer = -1
    length = len(dungeons)
    orders = [i for i in range(0, length)]
    sequences = list(permutations(orders, length))
    for sequence in sequences:
        cur_k = k
        count = 0
        for index in sequence:
            if cur_k >= dungeons[index][0]:
                count += 1
                cur_k -= dungeons[index][1]
                continue
            break
        answer = max(answer, count)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]) == 3)
