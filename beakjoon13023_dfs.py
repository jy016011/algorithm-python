import sys
input = sys.stdin.readline

def dfs(depth, node):
    global is_max
    #print(depth, node)
    if depth == 5:
        is_max = True
        return
    visited[node] = True
    for adj in graph[node]:
        if not visited[adj]:
            dfs(depth+1, adj)
    visited[node] = False

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)] # 0,....N nodes
visited = [False] * N
is_max = False
for _ in range(M):
    start, end = list(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)
# for i in range(len(graph)):
#     graph[i].sort()
#print(graph)

for i in range(N):
    dfs(1,i)
    if is_max:
        break
if is_max:
    print(1)
else: print(0)