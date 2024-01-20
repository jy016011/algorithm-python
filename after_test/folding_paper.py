def getHoles(start, end, cut, depth):
    global cnt
    paper[cut[0]][cut[1]] = 0
    # holes.append(cut)
    for i in range(depth, len(fold)):
        if not visited[i]:
            visited[i] = True
            if fold[i] == 1: #좌에서 우로 접기
                yMid = (start[1] + end[1]) // 2
                x = cut[0]
                y = end[1] - cut[1] + start[1]
                if cut[1] > yMid:
                    getHoles(start, [end[0], yMid], [x, y], depth + 1)
                    start = [start[0], yMid + 1]
                    cnt += 1
                else:
                    getHoles([start[0], yMid + 1], end, [x, y], depth + 1)
                    end = [end[0], yMid]
                    cnt += 1
            else: # 밑에서 위로 접기
                xMid = (start[0] + end[0]) // 2
                x = end[0] - cut[0] + start[0]
                y = cut[1]
                if cut[0] > xMid:
                    getHoles(start, [xMid, end[1]], [x, y], depth + 1)
                    start = [xMid + 1, start[1]]
                    cnt += 1
                else:
                    getHoles([xMid + 1, start[1]], end, [x, y], depth+ 1)
                    end = [xMid, end[1]]
                    cnt += 1
            visited[i] = False
            depth += 1

cnt = 0
fold = [1, -1, -1] # 1은 좌에서 우로 접기, -1은 밑에서 위로접기
# fold = [1, 1]
visited = [False for _ in range(len(fold))]
cuts = [[2, 2], [4, 4]]
# cuts = [[2,1]]
N = 8 # 높이
M = 6 # 너비
# N = 4
# M = 4
foldHeight = N
foldWide = M
paper = [[1] * (M + 1) for _ in range(N + 1)]
for act in fold: # 다 접은 후 길이 구하기
    if act == 1:
        foldWide = foldWide // 2
    elif act == -1:
        foldHeight = foldHeight // 2
for cut in cuts: # 다 접은 후 자를 수 없는 부분 찾기
    if cut[0] > foldHeight or cut[1] > foldWide:
        cuts.remove(cut)
# holes = []
for cut in cuts:
    # paper[cut[0]][cut[1]] = 0
    getHoles([1 ,1],[N, M], cut, 0)

# print(holes)
print(cnt)
for row in paper[1:]:
    print(row[1:])

