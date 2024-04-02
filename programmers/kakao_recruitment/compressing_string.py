def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        chars = []
        for start in range(0, len(s) - step + 1, step):
            chars.append(s[start:start + step])
        if len(s) % step != 0:
            chars.append(s[-(len(s) % step):])
        compressed = compress(chars)
        answer = min(answer, len(compressed))
    return answer


def compress(chars):
    total_compressed = ""
    idx = 0
    while idx < len(chars):
        cur = chars[idx]
        count = 0
        for following in chars[idx:]:
            if cur != following:
                break
            count += 1
            idx += 1
        else:
            idx += 1
        compressed = str(count) + cur if count > 1 else cur
        total_compressed += compressed
    return total_compressed


print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd") == 17)
print(solution("a") == 1)
