'''
프로그래머스 코딩테스트 고득점 kit 해시, 문제 4번: 의상
'''

global result
result = 0
global category_dict
category_dict = {}
global category_list


# passed 27 cases of total 28 cases, 1 case time out
def solution(clothes):
    for wear in clothes:
        if wear[1] in category_dict.keys():
            category_dict[wear[1]] += 1
            continue
        category_dict[wear[1]] = 1
    global category_list
    category_list = list(category_dict.keys())
    for i in range(1, len(category_list) + 1):
        backTracking(i, 0, 0, 1)
    return result


def backTracking(target_depth, start, depth, multi):
    global result
    if target_depth == depth:
        result += multi
    for i in range(start, len(category_list)):
        multi *= category_dict[category_list[i]]
        backTracking(target_depth, i + 1, depth + 1, multi)
        multi //= category_dict[category_list[i]]


# answer : 5
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
