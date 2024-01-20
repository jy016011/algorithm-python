def is_valid(r):
    #print(r, row)
    for n in range(r): # 0 to r-1 row
        if row[r] == row[n]: #n번째 행 퀸과 같은 열인지
            return False
        elif abs(r - n) == abs(row[r] - row[n]): #n번째 행 퀸과 행의 차, 열의 차가 같은지==대각선상에 있는경우
            return False
    return True
def put_queen(r):
    global count
    if r == N:
        count += 1
        #print("Nqueens",row)
        return
    for m in range(N): # 0 to N-1 col
        row[r] = m
        if is_valid(r):
            put_queen(r+1)# 다음행에 퀸 놓기

N = int(input())
row = [0] * N # row[i]'s value == board[i][row[i]]'s index
count = 0

put_queen(0)
print(count)