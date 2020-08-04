# 코딩테스트 연습 > 연습문제 > 콜라스 추측

def solution(num):
    cnt = 0
    while num > 1 and cnt < 500:
        if num & 1:
            num = num * 3 + 1
        else:
            num //= 2
        cnt += 1
    return cnt if cnt < 500 else -1