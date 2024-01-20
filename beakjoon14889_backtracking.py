import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global min_val
    if depth == (N//2):
        #print("st",start_team)
        ssum, lsum = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:#member in start team case
                    ssum += matrix[i][j]
                elif not visited[i] and not visited[j]:
                    lsum += matrix[i][j]
        sub = abs(ssum - lsum)
        min_val = min(min_val,sub)
        return
    for n in range(idx,N):
        if not visited[n]:
            visited[n] = True
            dfs(depth+1, idx +1)
            visited[n] = False


N = int(input())
min_val = N*100
visited =[False] * (N)
matrix = [list(map(int, input().split())) for _ in range(N)]

dfs(0,0)
print(min_val)