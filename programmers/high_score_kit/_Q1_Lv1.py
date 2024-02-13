def solution(nums):
    return min(len(nums) // 2, len(set(nums)))

print(solution([3, 3, 3, 2, 2, 4])) # answer: 3