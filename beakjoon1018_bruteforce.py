M, N = list(map(int, input().split()))
matrix = []
counts = []
for _ in range(M):
     matrix.append(input())

count = 0
for m in range(M-7):
     for n in range(N-7):
         drawB = 0
         drawW = 0
         for i in range(m,m+8):
             for j in range(n,n+8):
                if(i + j) % 2 == 0:
                    if matrix[i][j] != "B":
                        drawB += 1
                    if matrix[i][j] != "W":
                        drawW += 1
                else:
                    if matrix[i][j] != "W":
                        drawB += 1
                    if matrix[i][j] != "B":
                        drawW += 1

         counts.append(drawB)
         counts.append(drawW)
print(min(counts))

