import sys
input = sys.stdin.readline

scores = []
for i in range(8):
    scores.append([int(input()), i]) # scores[i] = {score, question_number}
scores.sort()
sum = 0
p = []
for i in range(len(scores) - 1, 2, -1):
    sum += scores[i][0]
    p.append(scores[i][1] + 1)
print(sum)
p.sort()
print(*p)
