N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))
min_sub = M
max_combi = 0
count = 0
for i in range(len(cards)):
    combi = []
    combi.append(cards[i])
    for j in range(i+1,len(cards)):
        if (cards[j] not in combi) and (j > i):
            #combi.append(cards[j])
            for k in range(j+1,len(cards)):
                if (cards[k] not in combi) and (k > j):
                    #combi.append(cards[k])
                    #count += 1
                    #print(combi)
                    sum1 = cards[i] + cards[j] + cards[k]
                    if sum1 <= M:
                        max_combi = max(max_combi, sum1)
                    #combi.pop()
            #combi.pop()
print(max_combi)

