def solution(tickets):
    routes = {}
    for src, dest in tickets:
        routes[src] = routes.get(src, []) + [dest]
    # 사전 순으로 먼저인 도착지를 뒤에서 pop하기 위해 역순 정렬
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or routes[top] == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    return path[::-1]
