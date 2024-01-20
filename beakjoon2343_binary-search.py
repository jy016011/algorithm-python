import sys
input = sys.stdin.readline

def check_size(blue_size, blue_cnt):
    cnt_needs = 1
    current_size = 0
    for i in range(0,len(lessons) - 1):
        current_size += lessons[i]
        future_size = current_size + lessons[i + 1]
        if future_size > blue_size:
            cnt_needs += 1
            current_size = 0
    if cnt_needs <= blue_cnt:
        return "ENOUGH"
    else:
        return "MORE"

ls_cnt, blue_cnt = list(map(int, input().split()))
lessons = list(map(int, input().split()))
result = 0

start = max(lessons)
end = sum(lessons)
mid = (start + end) // 2 # size of blue ray

while start <= end:
    if check_size(mid, blue_cnt) == "ENOUGH":
        result = mid
        end = mid - 1
        mid = (start + end) // 2
    elif check_size(mid, blue_cnt) == "MORE":
        start = mid + 1
        mid = (start + end) // 2

print(result)