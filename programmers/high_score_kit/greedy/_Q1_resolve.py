def solution(n, lost, reserve):
    # 양 끝 학생들의 경우를 고려하여 양 끝단에 1을 더 추가
    uniforms = [1] * (n + 2)
    for i in reserve:
        uniforms[i] += 1
    for i in lost:
        uniforms[i] -= 1
    for i in range(1, n + 1):
        if uniforms[i - 1] == 0 and uniforms[i] == 2:
            uniforms[i - 1:i + 1] = [1, 1]
        elif uniforms[i] == 2 and uniforms[i + 1] == 0:
            uniforms[i:i + 2] = [1, 1]

    return len([x for x in uniforms[1: -1] if x > 0])


def solution2(n, lost, reserve):
    s = set(lost) & set(reserve)
    # 체육복이 도난당한 학생들(여벌이 있는데 도난당한 학생들 제외)
    l = set(lost) - s
    # 여벌의 체육복이 있고, 도난당하지 않은 학생들
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)
