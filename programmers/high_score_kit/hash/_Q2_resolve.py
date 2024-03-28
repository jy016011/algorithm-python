def solution(participant, completion):
    p_dict = {}
    for p in participant:
        p_dict[p] = p_dict.get(p, 0) + 1

    for c in completion:
        p_dict[c] -= 1
    answer = [key for key, value in p_dict.items() if value > 0]
    return answer


from collections import Counter


def solution2(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    return list(dict(p_counter - c_counter).keys())[0]
