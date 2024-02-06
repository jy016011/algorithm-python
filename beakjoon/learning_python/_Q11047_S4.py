import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
count = 0
for i in range(len(coins) - 1, -1, -1):
    if K // coins[i] > 0:
        count += K // coins[i]
        K = K % coins[i]

print(count)
