a, b, c, d, e, f = list(map(int, input().split()))
result_x, result_y = 0,0
for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            result_x, result_y = x, y
            break
print(result_x, result_y)