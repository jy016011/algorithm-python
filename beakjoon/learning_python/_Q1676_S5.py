import sys
import math

input = sys.stdin.readline

N = int(input())

facto = math.factorial(N)

count = 0
isMetZero = False

while facto > 0:
    remain = facto % 10
    if remain == 0:
        count += 1
        isMetZero = True
    elif isMetZero:
        break
    facto //= 10

print(count)