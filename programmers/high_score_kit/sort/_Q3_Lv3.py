def solution(citations):
    answer = 0
    citations.sort()
    index = 0
    for i in range(len(citations)):
        if citations[i] <= len(citations) - i:
            answer = citations[i]
            index = i
            continue
        index = i
        break

    for h in range(answer, citations[index]):
        if h <= len(citations) - index:
            answer = h
    return answer


print(solution([3, 0, 6, 1, 5]) == 3)
print(solution([1, 2, 2, 2, 2, 2, 6, 6, 6, 7]) == 4)
print(solution([0, 0, 0]) == 0)
print(solution([0, 0, 1]) == 1)
print(solution([0, 1, 2, 2, 2]) == 2)
print(solution([3, 4]) == 2)
