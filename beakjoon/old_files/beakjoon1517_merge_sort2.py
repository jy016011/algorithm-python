# merge sort
def merge_sort(start, end): # sort start to end(not except end)
    global answer
    if start == end:
        return
    m = (end+start) // 2
    merge_sort(start, m)
    merge_sort(m + 1, end)
    idx1 = start # index of 'nums' list for num in subset1
    idx2 = m + 1 # index of 'nums' list for num in subset2
    k = start # index of 'nums' for valid number(sorted)
    for i in range(start, end + 1):
        temp[i] = nums[i] # just copy of subset of 'nums', not sorted.

    while (idx1 <= m) and (idx2 <= end): # sorting 'nums'
        if temp[idx1] > temp[idx2]:
            nums[k] = temp[idx2]
            answer = answer + idx2 - k
            k += 1
            idx2 += 1
        elif nums[idx1] <= nums[idx2]:
            nums[k] = temp[idx1]
            k += 1
            idx1 += 1
    if idx1 <= m: # for remain of subset1
        for i in range(idx1,m+1):
            nums[k] = temp[i]
            k += 1
    elif idx2 <= end: # for remain of subset2
        for i in range(idx2,end+1):
            nums[k] = temp[i]
            k += 1

N = int(input())
nums = []
temp = [0] * (N)
answer = 0 #result of total of swapping
nums = list(map(int, input().split()))
merge_sort(0,N-1)

print(answer)