def solution(s):
    answer = len(s)
    for size in range(1, len(s) // 2 + 1):
        count = 1
        compressed_size = 0
        prev = s[:size]
        for start in range(size, len(s) + size, size):
            cur = s[start: start + size]
            if prev == cur:
                count += 1
            else:
                compressed_size += size + len(str(count)) if count > 1 else len(prev)
                prev = cur
                count = 1
        answer = min(answer, compressed_size)
    return answer


print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd") == 17)
print(solution("a") == 1)
