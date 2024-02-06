import sys
input = sys.stdin.readline

K = int(input())
answer = ""
for _ in range(K):
    answer += "Class {0}\n".format(_ + 1)
    scores = list(map(int, input().split()))
    scores = scores[1:scores[0] + 1]
    scores.sort()
    maxGap = -sys.maxsize
    for i in range(len(scores) - 1):
        gap = scores[i + 1] - scores[i]
        maxGap = max(maxGap, gap)
    answer += "Max {0}, Min {1}, Largest gap {2}\n".format(scores[len(scores) - 1], scores[0], maxGap)

print(answer)