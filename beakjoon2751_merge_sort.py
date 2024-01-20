# merge sort
def merge_sort(start, end): # sort start to end(not except end)
    if start == end:
        return
    m = (end+start) // 2
    merge_sort(start, m)
    merge_sort(m + 1, end)
    idx1 = start # index of subset1
    idx2 = m + 1 # index of subset2
    temp = [] # buffer of sorted and merged subset

    while (idx1 <= m) and (idx2 <= end):
        #print(idx1,idx2)
        if nums[idx1] >= nums[idx2]:
            temp.append(nums[idx2])
            idx2 += 1
        elif nums[idx1] < nums[idx2]:
            temp.append(nums[idx1])
            idx1 += 1
    if idx1 <= m: # for remain of subset1
        for i in range(idx1,m+1):
            temp.append(nums[i])
    elif idx2 <= end: # for remain of subset2
        for i in range(idx2,end+1):
            temp.append(nums[i])
    #print("temp",temp)
    i = start
    for t in temp: # sorting numbers pasting from temp buffer
        nums[i] = t
        i += 1
    #print("nums",nums)


N = int(input())
nums = []
temp = [0] * N
for _ in range(N):
    nums.append(int(input()))
merge_sort(0,N-1)

for num in nums:
    print(num)