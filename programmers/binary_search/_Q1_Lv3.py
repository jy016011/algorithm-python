'''
프로그래머스 코딩테스트 고득점 kit 이분탐색, 문제 1번: 입국심
'''


def solution(n, times):
    lower_time = times[0]
    upper_time = times[len(times) - 1] * n
    answer = upper_time

    while lower_time <= upper_time:
        mid_time = (lower_time + upper_time) // 2
        passed = sum(list(map(lambda x: mid_time // x, times)))

        if passed >= n:
            upper_time = mid_time - 1
            answer = min(answer, mid_time)
        elif passed < n:
            lower_time = mid_time + 1

    return answer


print(solution(6, [7, 10]) == 28)
