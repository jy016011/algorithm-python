import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [False for _ in range(point+1)]
    visited[start] = True
    q = deque()
    q.append(start)
    bfs_list.append(start)
    while q:
        node = q.popleft()
        for v in graph[node]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True
                bfs_list.append(v)

def dfs(vertex):
    if dfs_visited[vertex] == False:
        dfs_visited[vertex] = True
        dfs_list.append(vertex)
        for v in graph[vertex]:
            dfs(v)
    else:
        return

input_line = list(map(int,input().split()))
point = input_line[0]
edge = input_line[1]
start = input_line[2]
bfs_list = list()
dfs_list = list()
dfs_visited = [False for _ in range(point+1)]

graph = [[] for _ in range(point+1)]
for _ in range(edge):
    start1, end = list(map(int,input().split()))
    graph[start1].append(end)
    graph[end].append(start1)

for i in range(len(graph)):
    graph[i].sort()

print(graph)
bfs()
dfs(start)
print(*dfs_list)
print(*bfs_list)
