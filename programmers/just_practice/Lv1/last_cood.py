def solution(v):
    x_cood = []
    y_cood = []
    for x, y in v:
        if x not in x_cood:
            x_cood.append(x)
        else:
            x_cood.remove(x)

        if y not in y_cood:
            y_cood.append(y)
        else:
            y_cood.remove(y)

    return x_cood + y_cood


def solution2(pos):
    x = pos[0][0] ^ pos[1][0] ^ pos[2][0]
    y = pos[0][1] ^ pos[1][1] ^ pos[2][1]
    return [x, y]


print(solution([[1, 4], [3, 4], [3, 10]]) == [1, 10])
print(solution([[1, 1], [2, 2], [1, 2]]) == [2, 1])

print(solution2([[1, 4], [3, 4], [3, 10]]) == [1, 10])
print(solution2([[1, 1], [2, 2], [1, 2]]) == [2, 1])
