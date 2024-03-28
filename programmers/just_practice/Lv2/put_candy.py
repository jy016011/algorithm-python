def solution(m, weights):
    answer = [0]
    backTracking(0, m, weights, answer)
    return answer.pop()


def backTracking(start, remain, weights, answer):
    if remain < 0:
        return

    if remain == 0:
        answer[0] += 1
        return

    for i in range(start, len(weights)):
        backTracking(i + 1, remain - weights[i], weights, answer)


print(solution(3000, [500, 1500, 2500, 1000, 2000]) == 3)
