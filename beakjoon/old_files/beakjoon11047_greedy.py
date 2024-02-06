import sys
input = sys.stdin.readline
N, K = list(map(int, input().split()))
units = []
cnt_coins = 0

for _ in range(N):
    units.append(int(input()))

for i in range(N - 1, -1, -1):
    if K == 0:
        break
    if units[i] > K:
        continue
    cnt_coins += (K // units[i])
    K = (K % units[i])

print(cnt_coins)