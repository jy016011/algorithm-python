N = int(input())
nums = []
for i in range(N):
    nums.append((int(input()),i))

sort_nums = sorted(nums)
#print(sort_nums)
max_val = 0
for i in range(len(nums)):
    if max_val < sort_nums[i][1] - i :
        max_val = sort_nums[i][1] - i
print(max_val+1)