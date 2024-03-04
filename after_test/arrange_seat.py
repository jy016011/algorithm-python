def count_arrangements(r, c, teams):
    people = []
    people_dict = {}
    visited = [[False] * c for _ in range(r)]
    for idx, team in enumerate(teams):
        members = team.split()
        people += members
        for member in members:
            people_dict[member] = idx + 1
    seated = [False] * len(people)
    print(people_dict)
    count = 0
    combis = ""
    matrix = [[0] * c for _ in range(r)]

    def dfs(depth, x, y, combi):
        nonlocal count, combis
        if depth == len(people):
            temp = ''.join(map(str, combi))
            if combis.find(temp) == -1:
                print(matrix)
                count += 1
                combis += ","
                combis += temp
            return

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                for p in range(len(people)):
                    if not seated[p]:
                        if isValid(nx, ny, p):
                            seated[p] = True
                            combi.append(p)
                            matrix[nx][ny] = p
                            dfs(depth + 1, nx, ny, combi)
                            seated[p] = False
                            combi.pop()
                            matrix[nx][ny] = 0
                visited[nx][ny] = False

    def isValid(x, y, index):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not canMove(nx, ny) or not visited[nx][ny]:
                continue
            if people_dict[people[matrix[nx][ny]]] == people_dict[people[index]]:
                return False
        return True

    def canMove(x, y):
        return not (x < 0 or y < 0 or x >= r or y >= c)

    dfs(0, 0, 0, [])
    print(count)


# testcases 3 of 4 cases pass
# should be 224 but, 336
r, c = 2, 3
teams = ["Willy Andy", "Green Ethan", "Nick", "Rok"]
count_arrangements(r, c, teams)

# answer: 8
r, c = 2, 2
teams = ["a", "b", "c d"]
count_arrangements(r, c, teams)

# answer: 2
r, c = 1, 2
teams = ["a", "b"]
count_arrangements(r, c, teams)

# answer : 0
r, c = 4, 4
teams = ["aa bb cc", "dd"]
count_arrangements(r, c, teams)
