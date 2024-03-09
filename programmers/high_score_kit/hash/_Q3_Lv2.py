'''
프로그래머스 코딩테스트 고득점 kit 해시, 문제 3번: 전화번호 목록
'''


def solution(phone_book):
    number_set = set([])
    for number in phone_book:
        number_set.add(number)

    for number in number_set:
        number_set.remove(number)
        for i in range(1, len(number) + 1):
            if (number[:i] in number_set):
                return False
        number_set.add(number)

    return True;


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))  # True
