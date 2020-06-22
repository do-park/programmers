# 코딩테스트 연습 > 연습문제 > 핸드폰 번호 가리기

def solution(phone_number):
    l = len(phone_number)
    answer = '*' * (l - 4) + str(phone_number[l - 4:l + 1])
    return answer