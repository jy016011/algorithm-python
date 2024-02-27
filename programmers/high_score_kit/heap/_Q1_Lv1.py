import heapq

'''
프로그래머스 코딩테스트 고득점 kit 힙, 문제 1번: 더 맵게
'''


def solution(scoville, K):
    answer = 0
    pq = []
    for s in scoville:
        heapq.heappush(pq, s)

    while True:
        least = heapq.heappop(pq)
        if least >= K:
            break
        if len(pq) == 0:
            return -1
        second = heapq.heappop(pq)
        newS = least + second * 2
        heapq.heappush(pq, newS)
        answer += 1
    return answer


# answer: 2
print(solution([1, 2, 3, 9, 10, 12], 7))
