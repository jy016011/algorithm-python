import sys
input = sys.stdin.readline

answer = ''
while True:
    n = int(input())
    if n == -1:
        break
    sum = 0
    answer += "{0} = ".format(n)
    for i in range(1, n):
        if n % i == 0:
            sum += i
            answer += "{0} + ".format(i)
    if sum == n:
        answer = answer[:-3]
        answer += "\n"
    else:
        answer = answer[:answer.rfind("\n") + 1]
        answer += "{0} is NOT perfect.\n".format(n)

print(answer)