from collections import deque

'''
프로그래머스 코딩테스트 PCCP 기출문제, 2번: 석유 시추
'''


def solution(land):
    answer = 0
    oil_dict = {}
    index = 1

    for y in range(len(land[0])):
        for x in range(len(land)):
            if land[x][y] == 1:
                area = bfs(x, y, land, index)
                oil_dict[index] = area
                index += 1

    for y in range(len(land[0])):
        visited = [False] * (index)
        area = 0
        for x in range(len(land)):
            if land[x][y] < 0 and not visited[-land[x][y]]:
                visited[-land[x][y]] = True
                area += oil_dict[-land[x][y]]
        answer = max(answer, area)

    return answer


def bfs(start_x, start_y, land, index):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    area = 1
    queue = deque()
    queue.append([start_x, start_y])
    land[start_x][start_y] = -index

    while queue:
        current = queue.popleft()
        x = current[0]
        y = current[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(land) or ny >= len(land[0]):
                continue
            if land[nx][ny] == 1:
                area += 1
                queue.append([nx, ny])
                land[nx][ny] = -index

    return area
