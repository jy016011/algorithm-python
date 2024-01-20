import sys
from collections import deque
input = sys.stdin.readline

def dfs(now):
    visited[now] = True
    print(now,end=' ')
    for adj in graph[now]:
        if not visited[adj]:
            dfs(adj)

def bfs(start):
    visited[start] = True
    queue = deque([start])
    while queue:
        visited_node = queue.popleft()
        print(visited_node, end=' ')
        for adj in graph[visited_node]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)

N, M, n_start = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
for _ in range(M):
    start, end = list(map(int,input().split()))
    graph[start].append(end)
    graph[end].append(start)
for i in range(1,len(graph)):
    graph[i].sort()

dfs(n_start)
visited = [False] * (N + 1)
print()
bfs(n_start)