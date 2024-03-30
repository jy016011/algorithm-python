def solution(dirs):
    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    s = set()
    x = y = 0
    for dir in dirs:
        nx = x + directions[dir][1]
        ny = y + directions[dir][0]
        if nx < -5 or ny < -5 or nx > 5 or ny > 5:
            continue
        s.add((x, y, nx, ny))
        s.add((nx, ny, x, y))
        x, y = nx, ny

    return len(s) // 2


print(solution("ULURRDLLU") == 7)
print(solution("LULLLLLLU") == 7)
print(solution("UDUDUD") == 1)
