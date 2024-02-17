def solution(clothes):
    category_dict = {}
    answer = 1
    for wear in clothes:
        if wear[1] in category_dict.keys():
            category_dict[wear[1]] += 1
            continue
        category_dict[wear[1]] = 1
    for key in category_dict.keys():
        answer *= (category_dict[key] + 1)

    return answer - 1

# answer : 5
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))