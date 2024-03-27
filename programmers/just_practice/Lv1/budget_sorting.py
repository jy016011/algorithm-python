# sorting
def solution(d, budget):
    answer = 0
    d.sort()
    for request in d:
        if budget >= request:
            budget -= request
            answer += 1
    return answer


print(solution([1, 3, 2, 5, 4], 9) == 3)
print(solution([2, 2, 3, 3], 10) == 4)
