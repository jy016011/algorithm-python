isDone = False

'''
프로그래머스 코딩테스트 고득점 kit 완전탐색, 문제 7번: 모음사전
'''


def solution(word):
    answer = dfs(0, "", 0, word)
    return answer


def dfs(depth, word, index, target):
    global isDone
    if word == target:
        isDone = True
        return index
    if depth == 5:
        return index
    for ch in ['A', 'E', 'I', 'O', 'U']:
        word += ch
        index += 1
        index = dfs(depth + 1, word, index, target)
        if isDone:
            return index
        word = word[:-1]
    return index


print(solution("AAAAE") == 6)
isDone = False
print(solution("AAAE") == 10)
isDone = False
print(solution("I") == 1563)
