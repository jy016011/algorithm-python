nums = list(map(int, input()))
idx = 0
for i in range(len(nums)):
    max = i
    for j in range(i+1,len(nums)):
        if nums[max] < nums[j]:
            max = j
    if nums[i] < nums[max]:
        temp = nums[i]
        nums[i] = nums[max]
        nums[max] = temp

for num in nums:
    print(num,end='')
