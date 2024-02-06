import sys
input = sys.stdin.readline

T = int(input())
answer = ''
for i in range(T):
    A, B = map(int, input().split())
    answer += "Case #{0}: {1}\n".format(i + 1, A + B)

print(answer)