def solution(s):
    opens = []
    for ch in s:
        if ch is '(':
            opens.append(ch)
        elif ch is ')':
            if len(opens) == 0:
                return False
            opens.pop()


    return len(opens) == 0

