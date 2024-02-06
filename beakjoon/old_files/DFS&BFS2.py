from collections import deque

dfs_list = []
bfs_list = []
def dfs(graph, start, visited_list):
    visited_list[start] = True
    dfs_list.append(start)
    #print(start,end=' ')
    for adj in graph[start]:
        if not visited_list[adj]:
            dfs(graph,adj,visited_list)

def bfs(graph, start, visited_list):
    queue = deque([start])
    visited_list[start] = True
    while queue:
        visited_node = queue.popleft()
        bfs_list.append(visited_node)
        #print(visited_node, end=' ')
        for adj in graph[visited_node]:
            if not visited_list[adj]:
                queue.append(adj)
                visited_list[adj] = True


def init_visited_list(node_cnt):
    visited_list = [None]
    for node in range(node_cnt):
        visited_list.append(False)
    return visited_list

node_cnt, line_cnt, start = list(map(int,input().split()))
graph = [[] for _ in range(node_cnt+1)] # N+1 x N+1
for i in range(line_cnt):
    lstart, lend = list(map(int, input().split()))
    graph[lstart].append(lend)
    graph[lend].append(lstart)
visited_list = init_visited_list(node_cnt)
for node in graph:
    node.sort()

print(graph)
dfs(graph, start, visited_list)
visited_list = init_visited_list(node_cnt)
bfs(graph, start, visited_list)
print(*dfs_list)
print(*bfs_list)
