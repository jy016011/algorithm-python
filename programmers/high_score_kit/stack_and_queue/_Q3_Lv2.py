import queue


def solution(priorities, location):
    process_queue = queue.Queue()
    for i in range(len(priorities)):
        process_queue.put([i, priorities[i]])
    answer = 0
    while not process_queue.empty():
        current_process = process_queue.get()
        if any(process[1] > current_process[1] for process in process_queue.queue):
            process_queue.put(current_process)
        else:
            answer += 1
            if current_process[0] == location:
                break

    return answer


# answer: 1
print(solution([2, 1, 3, 2], 2))
# answer: 5
print(solution([1, 1, 9, 1, 1, 1], 0))
# answer: 1
print(solution([1, 1, 9, 1, 1, 1], 2))
