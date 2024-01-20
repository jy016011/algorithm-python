positive_lst = [0] * int(1e6+1)
negative_lst = [0] * int(1e6)
N = int(input())
for i in range(N):
    number = int(input())
    if number < 0:
        negative_lst[number] = 1
    else:
        positive_lst[number] = 1

for i in range(-1000000,1000001):
    if (i < 0) and (negative_lst[i] == 1):
        print(i)
    elif (i >= 0) and (positive_lst[i] == 1):
        print(i)



