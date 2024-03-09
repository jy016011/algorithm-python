import collections

'''
프로그래머스 코딩테스트 고득점 kit 해시, 문제 2번: 완주하지 못한 선수
'''


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]


# answer: "mislav"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
