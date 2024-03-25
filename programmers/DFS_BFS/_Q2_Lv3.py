from collections import deque

'''
프로그래머스 코딩테스트 고득점 kit 깊이/너비 우선 탐색, 문제 2번: 네트워크
'''


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for pc in range(len(computers)):
        if not visited[pc]:
            answer += 1
            bfs(pc, visited, computers)
    return answer


def bfs(start_pc, visited, computers):
    queue = deque()
    queue.append(start_pc)
    visited[start_pc] = True
    while queue:
        current_pc = queue.popleft()
        for pc in range(len(computers[current_pc])):
            if not visited[pc] and computers[current_pc][pc] == 1:
                visited[pc] = True
                queue.append(pc)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
