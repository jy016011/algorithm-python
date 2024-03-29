import heapq

"""
Dijkstra algorithm implementation in two ways
1. Linear search
2. Heapq
"""


def dijkstra_linear_search(n, edges, start):
    visited = [False] * (n + 1)
    distances = [float('inf')] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for src, dest, distance in edges:
        graph[src].append((distance, dest))
        graph[dest].append((distance, src))

    visited[start] = True
    distances[start] = 0

    for cost, next_node in graph[start]:
        distances[next_node] = cost

    for _ in range(n - 1):
        # 방문하지 않은 노드 중 최소거리 노드 가져오기
        cur_node, cur_cost = get_min_cost_node(visited, distances)
        # 가져온 노드의 인접 노드들의 최소 cost 갱신
        for cost, next_node in graph[cur_node]:
            next_cost = cost + cur_cost
            distances[next_node] = min(distances[next_node], next_cost)

    answer = ''
    for destination, distance in enumerate(distances[1:], start=1):
        answer += 'from #{} node to #{} node cost: {}\n'.format(start, destination, distance)
    return answer


def get_min_cost_node(visited, distances):
    min_val = float('inf')
    min_node = -1
    for node in range(1, n + 1):
        if not visited[node] and distances[node] < min_val:
            min_val = distances[node]
            min_node = node
    return min_node, min_val


def dijkstra_heapq(n, edges, start):
    distances = [float('inf')] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for src, dest, distance in edges:
        graph[src].append((distance, dest))
        graph[dest].append((distance, src))
    pq = []
    heapq.heappush(pq, (0, start))
    distances[start] = 0
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_cost > distances[cur_node]:
            continue
        for dist, next_node in graph[cur_node]:
            next_cost = cur_cost + dist
            if next_cost < distances[next_node]:
                distances[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))

    answer = ''
    for destination, distance in enumerate(distances[1:], start=1):
        answer += 'from #{} node to #{} node cost: {}\n'.format(start, destination, distance)

    return answer


edges = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
n = 5
print(dijkstra_linear_search(n, edges, 1))
print(dijkstra_heapq(n, edges, 1))
