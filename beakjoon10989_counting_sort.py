import sys
input = sys.stdin.readline
N = int(input())
counting_nums = [0] * 10001

for _ in range(N):
    counting_nums[int(input())] += 1

for number in range(10001):
    if counting_nums[number] != 0:
        for _ in range(counting_nums[number]):
            print(number)