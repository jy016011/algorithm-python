import sys
input = sys.stdin.readline

number_string = input().rstrip()

numbers = []
for ch in number_string:
    numbers.append(ch)
numbers.sort()
numbers.reverse()
print(''.join(numbers))