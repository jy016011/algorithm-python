'''
프로그래머스 코딩테스트 고득점 kit 해시, 문제 1번: 폰켓몬
'''


def solution(nums):
    return min(len(nums) // 2, len(set(nums)))


print(solution([3, 3, 3, 2, 2, 4]))  # answer: 3
