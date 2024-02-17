import queue


def solution(bridge_length, weight, truck_weights):
    trucks = queue.Queue()
    for truck in truck_weights:
        trucks.put([truck, 0])  # weight, distance
    onBridge = queue.Queue()
    remain_weight = weight
    answer = 0
    while not (trucks.empty() and onBridge.empty()):
        if not trucks.empty() and remain_weight >= trucks.queue[0][0]:
            remain_weight -= trucks.queue[0][0]
            onBridge.put(trucks.get())

        for truck in onBridge.queue:
            truck[1] += 1
        if not onBridge.empty() and onBridge.queue[0][1] == bridge_length:
            remain_weight += onBridge.get()[0]
        answer += 1

    return answer + 1


# answer: 8
print(solution(2, 10, [7, 4, 5, 6]))
# answer: 101
print(solution(100, 100, [10]))
# answer: 110
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
