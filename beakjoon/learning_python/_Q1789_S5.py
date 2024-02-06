import sys
input = sys.stdin.readline

S = int(input())

sum = 0
N = 1

while N * (N + 1) // 2 <= S :
    sum += N
    N += 1

print(N - 1)