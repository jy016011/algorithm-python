def solution(N, number):
    # s는 N을 x번 이용해서 만든 수들의 집합을 8개까지 저장
    s = [set() for x in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer
