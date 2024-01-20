import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
for i in range(M):
    start, end = list(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)
# dfs_list = []
result = 0
def dfs(node):
    visited[node] = True
    # dfs_list.append(node)
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj)

# print(graph)
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        result += 1
# print(dfs_list)
print(result)
