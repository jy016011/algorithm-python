def solution(numbers):
    numbers = list(map(str, numbers))
    return str(int(''.join(sorted(numbers, key=lambda x: (x * 4)[:4], reverse=True))))
