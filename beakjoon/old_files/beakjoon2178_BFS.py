import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visited[start][end] = True
    queue = deque([(start,end,graph[start][end])])
    while queue:
        row, col, depth = queue.popleft()
        #print(row, col)
        if row == N and col == M:
            break
        if (graph[row + 1][col] == 1) and not visited[row + 1][col]: # to down
            visited[row + 1][col] = True
            graph[row + 1][col] += depth
            queue.append((row + 1, col,graph[row + 1][col]))
        if (graph[row][col + 1] == 1) and not visited[row][col + 1]: # to right
            visited[row][col + 1] = True
            graph[row][col + 1] += depth
            queue.append((row, col + 1, graph[row][col + 1]))
        if (graph[row - 1][col] == 1) and not visited[row - 1][col]: # to up
            visited[row - 1][col] = True
            graph[row - 1][col] += depth
            queue.append((row - 1, col, graph[row - 1][col]))
        if (graph[row][col - 1] == 1) and not visited[row][col - 1]: # to left
            visited[row][col - 1] = True
            graph[row][col - 1] += depth
            queue.append((row, col - 1, graph[row][col - 1]))

N, M = list(map(int, input().split()))
graph = [[0] * (M + 2) for _ in range(N + 2)]
visited = [[False] * (M + 2) for _ in range(N + 2)]

for i in range(1, N+1):
    lst = list(input().strip())
    for j in range(0,len(lst)):
        graph[i][j+1] = int(lst[j])

# print(graph)
bfs(1,1)
print(graph[N][M])