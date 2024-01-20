from collections import deque
def draw_graph(node_cnt, lines):
    graph =[[]]
    for node_num in range(1,node_cnt+1):
        temp = []
        for line in lines:
            if node_num in line:
                for node in line:
                    if node != node_num:
                        temp.append(node)
        temp.sort()
        graph.append(temp)
    return graph

def dfs(graph, start, visited_list):
    visited_list[start] = True
    print(start,end=' ')
    for i in graph[start]:
        if not visited_list[i]:
            dfs(graph,i,visited_list)

def bfs(graph, start, visited_list):
    queue = deque([start])
    visited_list[start] = True
    while queue:
        visited_node = queue.popleft()
        print(visited_node, end=' ')
        for adj in graph[visited_node]:
            if visited_list[adj] is False:
                queue.append(adj)
                visited_list[adj] = True

def init_visited_list(node_cnt):
    visited_list = [None]
    for node in range(node_cnt):
        visited_list.append(False)
    return visited_list

lines = []
node_cnt, line_cnt, start = list(map(int,input().split()))
for i in range(line_cnt):
    lines.append(list(map(int, input().split())))

visited_list = init_visited_list(node_cnt)
graph = draw_graph(node_cnt,lines)
# print(graph)
dfs(graph, start, visited_list)
print()
visited_list = init_visited_list(node_cnt)
bfs(graph, start, visited_list)
