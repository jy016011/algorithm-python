def get_blank():
    for i in range(9):
        for j in range(9):
            if sdoku[i][j] == 0:
                blanks.append((i,j))

def fill_blank(idx):
    # for row in sdoku:
    #     print(*row)
    #print()
    if idx == len(blanks):
        return
    for i in range(1,10):
        blank_row = blanks[idx][0]
        blank_col = blanks[idx][1]
        if row_valid(blank_row, i) and col_valid(blank_col, i) and square_valid(blank_row, blank_col, i):
            sdoku[blank_row][blank_col] = i
            fill_blank(idx+1)
            #sdoku[blank_row][blank_col] = 0

def row_valid(row, number):
    for i in range(9):
        if sdoku[row][i] == number:
            return False
    return True

def col_valid(col, number):
    for i in range(9):
        if sdoku[i][col] == number:
            return False
    return True

def square_valid(row, col, number):
    square_start_row = (row // 3) * 3
    square_start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sdoku[square_start_row+i][square_start_col+j] == number:
                return False
    return True
sdoku = []
blanks = []
for i in range(9):
    sdoku_row = list(map(int, input().split()))
    sdoku.append(sdoku_row)

get_blank()
fill_blank(0)
for row in sdoku:
    print(*row)