'''
프로그래머스 코딩테스트 고득점 kit 탐욕법, 문제 1번: 체육복
'''


def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    visited = [False] * (n + 1)
    for l in lost:
        for r in reserve:
            if l == r:
                visited[r] = True
                break
    for l in lost:
        if not visited[l]:
            isBorrowed = False
            for r in reserve:
                if (l - 1 == r or l + 1 == r) and not visited[r]:
                    visited[r] = True
                    isBorrowed = True
                    break
            if not isBorrowed:
                answer -= 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
print(solution(3, [3], [1]) == 2)
print(solution(
    30,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
      )
