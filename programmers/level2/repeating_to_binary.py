def solution(s):
    answer = []
    binary = int(s)
    total_count = 0
    count_of_loop = 0
    while binary > 1:
        count_of_zero = 0
        for ch in s:
            if ch == '0':
                count_of_zero += 1
        total_count += count_of_zero
        binary = (len(s) - count_of_zero)
        s = str(bin(binary))[2:]
        count_of_loop += 1

    answer.append(count_of_loop)
    answer.append(total_count)
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))