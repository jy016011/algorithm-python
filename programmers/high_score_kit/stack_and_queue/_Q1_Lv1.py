def solution(arr):
    answer = []
    for num in arr:
        if answer[-1:] == [num]:
            continue
        answer.append(num)
    return answer

# answer: [1, 3, 0, 1]
print(solution([1, 1, 3, 3, 0, 1, 1]))

# answer: [4, 3]
print(solution([4, 4, 4, 3, 3]))