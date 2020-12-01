# 코딩테스트 연습 > 해시 > 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    for number1, number2 in zip(phone_book, phone_book[1:]):
        if number2.startswith(number1):
            return False
    return True


print(solution(['119', '97674223', '1195524421']))
print(solution(['123', '456', '789']))
print(solution(['12', '123', '1235', '567', '88']))
