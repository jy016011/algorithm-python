import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]

# answer: "mislav"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))