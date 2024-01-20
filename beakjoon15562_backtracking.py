def dfs(number):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for n in range(1, N+1):
        if n < number :
            continue
        s.append(n)
        dfs(n)
        s.pop()

N, M = list(map(int, input().split()))
s = []
dfs(1)