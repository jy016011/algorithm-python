weight = int(input())
remain = weight
bags = []
unit = 5
result = -1
while remain:
    if (sum(bags) <= weight) and (remain >= 5):
        unit = 5
        bags.append(unit)
        #print(bags)
        remain -= unit
    elif (sum(bags) <= weight) and (remain >= 3):
        unit = 3
        bags.append(unit)
        #print(bags)
        remain -= unit
    elif (0 < remain < 3) and (5 in bags):
        unit = 3
        for i in range(len(bags)):
            if bags[i] == 5:
                bags[i] = unit
                #print(bags)
                remain += 2
                break
    elif (remain < 3) and (5 not in bags):
        break
    if remain == 0:
        result = len(bags)
        break
print(result)