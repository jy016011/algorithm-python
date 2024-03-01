from collections import deque

'''
프로그래머스 코딩테스트 고득점 kit 완전탐색, 문제 6번: 전력망을 둘로 나누기
'''


def solution(n, wires):
    graph = [[] for i in range(n + 1)]

    for wire in wires:
        start = wire[0]
        end = wire[1]
        graph[start].append(end)
        graph[end].append(start)

    answer = n
    for wire in wires:
        start = wire[0]
        end = wire[1]
        graph[start].remove(end)
        graph[end].remove(start)
        visited = [False] * len(graph)
        area = []
        for node in range(1, n + 1):
            if not visited[node]:
                visited[node] = True
                area.append(bfs(graph, node, visited))
        answer = min(answer, abs(area[0] - area[1]))
        graph[start].append(end)
        graph[end].append(start)

    return answer


def bfs(graph, startNode, visited):
    q = deque()
    q.appendleft(startNode)
    cnt = 1
    while len(q) > 0:
        current = q.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                q.appendleft(next)
                cnt += 1
    return cnt


print(
    solution(
        9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
    ) == 3
)
