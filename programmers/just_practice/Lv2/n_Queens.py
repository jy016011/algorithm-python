def solution(n):
    queens = []
    return put_queen(queens, n, 0)


def put_queen(queens, n, row):
    answer = 0
    if row == n:
        return 1
    for c in range(n):
        if isValid(queens, row, c):
            queens.append((row, c))
            answer += put_queen(queens, n, row + 1)
            queens.pop()
    return answer


def isValid(queens, row, col):
    for before_row, before_col in queens:
        if col == before_col:
            return False
        if abs(before_row - row) == abs(before_col - col):
            return False
    return True


print(solution(4) == 2)
