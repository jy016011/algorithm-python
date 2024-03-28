def solution(number, k):
    stack = []
    for digit in number:
        while stack and stack[-1] < digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0 and stack:
        stack.pop()
        k -= 1
    return ''.join(stack)


def solution2(number, k):
    collected = []
    for i, num in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    return ''.join(collected)
