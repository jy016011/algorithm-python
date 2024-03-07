from itertools import permutations


def count_arrangements(r, c, teams):
    people = []
    people_dict = {}
    for idx, team in enumerate(teams):
        members = team.split()
        people += members
        for member in members:
            people_dict[member] = idx + 1
    count = 0
    permute = list(permutations([i for i in range(1, len(people) + 1)], len(people)))

    def is_valid(x, y, idx):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not canMove(nx, ny) or matrix[nx][ny] == 0:
                continue
            if people_dict[people[matrix[nx][ny] - 1]] == people_dict[people[idx]]:
                return False
        return True

    def canMove(x, y):
        return not (x < 0 or y < 0 or x >= r or y >= c)

    for position in permute:
        index = 0
        is_valid_position = True
        matrix = [[0] * c for _ in range(r)]
        for x in range(r):
            for y in range(c):
                if matrix[x][y] == 0 and is_valid(x, y, position[index] - 1):
                    matrix[x][y] = position[index]
                    index += 1
                    continue
                is_valid_position = False
                break
        if is_valid_position:
            count += 1
    # print(count)
    return count


# all test cases pass
r, c = 2, 3
teams = ["Willy Andy", "Green Ethan", "Nick", "Rok"]
print(count_arrangements(r, c, teams) == 224)

# answer: 8
r, c = 2, 2
teams = ["a", "b", "c d"]
print(count_arrangements(r, c, teams) == 8)

# answer: 2
r, c = 1, 2
teams = ["a", "b"]
print(count_arrangements(r, c, teams) == 2)

answer: 0
r, c = 2, 2
teams = ["aa bb cc", "dd"]
print(count_arrangements(r, c, teams) == 0)
