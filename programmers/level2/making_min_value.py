def solution(A,B):
    A.sort()
    B.sort()
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[-(i + 1)]
    return answer

def getMinSum(A, B): # same solution
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])



print(solution([1,4,2],[5,4,4]))
print(solution([1,2],[3,4]))
print(getMinSum([1,4,2],[5,4,4]))
print(getMinSum([1,2],[3,4]))