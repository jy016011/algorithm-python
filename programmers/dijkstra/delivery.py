import heapq


def solution(N, road, K):
    answer = 0
    distances = [float('inf')] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, 1))
    distances[1] = 0
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        for src, dest, dist in road:
            next_cost = cur_cost + dist
            if cur_node == src and next_cost < distances[dest]:
                distances[dest] = next_cost
                heapq.heappush(queue, (next_cost, dest))
            elif cur_node == dest and next_cost < distances[src]:
                distances[src] = next_cost
                heapq.heappush(queue, (next_cost, src))
    print(distances)
    return len([delivered for delivered in distances if delivered <= K])


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
