# 코딩테스트 연습 > 해시 > 전화번호 목록

def solution(phone_book):
    phone_book.sort(reverse=True)
    phone_dict = {}
    for phone_number in phone_book:
        phone_dict[phone_number] = 1
    for phone_number in phone_book:
        if phone_number in phone_dict:
            temp = ''
            for number in phone_number:
                temp += number
                if temp in phone_dict and temp != phone_number:
                    return False
    return True


print(solution(['119', '97674223', '1195524421']))
print(solution(['123', '456', '789']))
print(solution(['12', '123', '1235', '567', '88']))
