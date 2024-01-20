weight = int(input())
count = 0
while weight >= 0 :
    if (weight % 5) == 0:
        count += (weight // 5)
        print(count)
        break
    weight -= 3
    count += 1

else: print(-1)
