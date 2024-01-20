def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for n in range(1, N+1):
        #if visited[n]:
        #    continue
        #visited[n] = True
        s.append(n)
        dfs()
        s.pop()
        #visited[n] = False

N, M = list(map(int, input().split()))
s = []
#visited = [False] * (N+1)
dfs()