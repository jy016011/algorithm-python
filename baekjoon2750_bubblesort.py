N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for i in range(N-1):
    for j in range(N-1-i):
        if nums[j] > nums[j+1]:
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp
for num in nums:
    print(num)