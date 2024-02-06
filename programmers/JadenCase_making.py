def solution(s):
    answer =''
    strList = s.split()
    for i in range(len(strList)):
        strList[i] = strList[i].capitalize()
    answer = ' '.join(strList)
    return answer