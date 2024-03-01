'''
프로그래머스 코딩테스트 고득점 kit 완전탐색, 문제 2번: 모의고사
'''


def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_dict = {1: 0, 2: 0, 3: 0}
    result = []

    for index, answer in enumerate(answers):
        if answer == first[index % len(first)]:
            answer_dict[1] += 1
        if answer == second[index % len(second)]:
            answer_dict[2] += 1
        if answer == third[index % len(third)]:
            answer_dict[3] += 1

    for student, count in answer_dict.items():
        if count == max(answer_dict.values()):
            result.append(student)
    return result


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
