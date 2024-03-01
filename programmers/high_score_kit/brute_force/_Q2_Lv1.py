from collections import deque

'''
프로그래머스 코딩테스트 고득점 kit 완전탐색, 문제 2번: 모의고사
'''


def solution(answers):
    first = deque([1, 2, 3, 4, 5])
    second = deque([2, 1, 2, 3, 2, 4, 2, 5])
    third = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    answer_dict = {1: 0, 2: 0, 3: 0}
    for answer in answers:
        first_ans = first.popleft()
        second_ans = second.popleft()
        third_ans = third.popleft()
        if first_ans == answer:
            answer_dict[1] += 1
        if second_ans == answer:
            answer_dict[2] += 1
        if third_ans == answer:
            answer_dict[3] += 1
        first.append(first_ans)
        second.append(second_ans)
        third.append(third_ans)

    max_value = max(answer_dict.values())
    result = []
    for key in answer_dict.keys():
        if answer_dict[key] == max_value:
            result.append(key)
    return result


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
