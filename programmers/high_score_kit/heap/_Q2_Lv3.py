from collections import deque
import heapq

'''
프로그래머스 코딩테스트 고득점 kit 힙, 문제 2번: 디스크 컨트롤러
'''


def solution(jobs):
    answer = 0
    # duration, start time
    jobDeque = deque(sorted([(job[1], job[0]) for job in jobs], key=lambda x: (x[1], x[0])))

    schedule = []
    heapq.heappush(schedule, jobDeque.popleft())
    endTime = 0
    while len(schedule) > 0:
        job = heapq.heappop(schedule)
        endTime = max(endTime + job[0], job[1] + job[0])
        answer += (endTime - job[1])

        while len(jobDeque) > 0:
            if jobDeque[0][1] <= endTime:
                heapq.heappush(schedule, jobDeque.popleft())
                continue
            break

        if len(schedule) == 0 and len(jobDeque) > 0:
            heapq.heappush(schedule, jobDeque.popleft())

    return answer // len(jobs)


# answer: 9
print(solution([[0, 3], [1, 9], [2, 6]]))
# answer: 5
print(solution([[1, 4], [7, 9], [1000, 3]]))
