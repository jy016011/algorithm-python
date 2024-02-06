import sys
input = sys.stdin.readline
def dfs(depth, number, add, sub, multiply, divide):
    global max_val, min_val
    if depth == N: # N-1번 연산 후 최대, 최소값 갱신
        max_val = max(number,max_val)
        min_val = min(number,min_val)
        return

    if add:
        dfs(depth + 1, number + nums[depth], add - 1, sub, multiply, divide)
    if sub:
        dfs(depth + 1, number - nums[depth], add, sub - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, number * nums[depth], add, sub, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(number / nums[depth]), add, sub, multiply, divide - 1)

min_val = int(1e9)
max_val = int(-1e9)

N = int(input())
nums = list(map(int, input().split()))
add, sub, multiply, divide = list(map(int, input().split()))

dfs(1, nums[0], add, sub, multiply, divide)
print(max_val)
print(min_val)