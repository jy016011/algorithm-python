import sys
input = sys.stdin.readline

T = int(input())
answer = ''
for _ in range(T):
    N = int(input())
    a = {}
    for n in range(N):
        S, L = input().split()
        L = int(L)
        a[L] = S
    maxKey = max(a.keys())
    answer += a[maxKey] + "\n"

print(answer)