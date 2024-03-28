def solution(max_weight, specs, names):
    answer = 1
    spec_dict = dict(specs)
    remain_weight = max_weight
    for product in names:
        weight = int(spec_dict[product])
        if remain_weight < weight:
            answer += 1
            remain_weight = max_weight
        remain_weight -= weight
    return answer


print(solution(300, [["toy", "70"], ["snack", "200"]], ["toy", "snack", "snack"]) == 2)
print(solution(200, [["toy", "70"], ["snack", "200"]], ["toy", "snack", "toy"]) == 3)
