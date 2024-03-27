from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    queue = deque()
    for progress, speed in zip(progresses, speeds):
        remain_pr = 100 - progress
        remain_time = math.ceil(remain_pr / speed)
        queue.append((progress, remain_time))
    before_time = queue[0][1] if queue else 0
    count = 0
    while queue:
        cur_time = queue.popleft()[1]
        if cur_time <= before_time:
            count += 1
        else:
            answer.append(count)
            before_time = cur_time
            count = 1
    answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]) == [2, 1])
