nums = [1,2,3,4]
visited = [False] * len(nums)
combi = []
answer = 0
def dfs(idx):
    global answer
    if len(combi) == 3:
        print(combi)
        if isPrime(sum(combi)):
            answer += 1
        return

    for i in range(idx, len(nums)):
        if not visited[i]:
            visited[i] = True
            combi.append(nums[i])
            dfs(i+1)
            combi.pop()
            visited[i] = False

def isPrime(num):
    for i in range(2 , int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

dfs(0)
print(answer)
