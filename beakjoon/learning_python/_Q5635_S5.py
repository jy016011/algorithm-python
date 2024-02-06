import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    name, d, m, y = input().rstrip().split()
    d, m, y = map(int, (d, m, y))
    people.append([y, m, d, name])

people.sort()
print(people[-1][3])
print(people[0][3])