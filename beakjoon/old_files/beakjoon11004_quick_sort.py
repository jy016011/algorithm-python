#used_quick_sort
N, K = list(map(int,input().split()))
nums = list(map(int,input().split()))
def quick_sort(start, end, K):
    if start < end:
        pivot = get_pivot(start,end)
        #print(pivot, nums)
        if pivot == K:
            return
        elif pivot > K:
            quick_sort(start, pivot - 1, K)
        else:
            quick_sort(pivot + 1, end, K)

def get_pivot(start, end):
    if (end - start) == 1:
        if nums[start] > nums[end]:
            swap(start,end)
        return end
    elif start == end:
        return end

    M = (end + start) // 2
    swap(start,M)
    i = start + 1
    j = end
    while i <= j:
        #print("loop start", "i",i,"j",j,nums)
        while (nums[j] > nums[start]) and (j > 0):
            j -= 1
        while (nums[i] < nums[start]) and (i < len(nums)-1):
            i += 1
        if i < j:
            swap(i, j)

    pivot = nums[start]
    nums[start] = nums[j]
    nums[j] = pivot
    #print("before return",nums)
    return j

def swap(x,y):
    temp = nums[x]
    nums[x] = nums[y]
    nums[y] = temp

quick_sort(0, N-1, K-1)
print(nums[K-1])