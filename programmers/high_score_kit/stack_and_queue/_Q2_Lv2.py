import queue
def solution(progresses, speeds):
    answer = []
    progresses_queue = queue.Queue()
    for i in range(len(progresses)) :
        remain = 100 - progresses[i]
        if remain % speeds[i] == 0:
            remain //= speeds[i]
        else:
            remain = (remain // speeds[i]) + 1
        progresses_queue.put(remain)

    while not progresses_queue.empty():
        current_day = progresses_queue.get()
        count = 1
        while not progresses_queue.empty() and progresses_queue.queue[0] <= current_day:
            progresses_queue.get()
            count += 1
        answer.append(count)
    return answer


# answer: [2, 1]
print(solution([93, 30, 55], [1, 30, 5]))
# answer: [1, 3, 2]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))