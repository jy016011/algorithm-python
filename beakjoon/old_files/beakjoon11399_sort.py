#insertion sort
N = int(input())
times = list(map(int, input().split()))
for i in range(1,N): # 1 to N-1
    for j in range(i,0,-1):
        if times[j] < times[j-1]:
            times[j] , times[j-1] = times[j-1], times[j]


total_t = 0
for i in range(1,len(times)+1):
    total_t += sum(times[0:i])
print(total_t)
