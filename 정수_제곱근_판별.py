# 코딩테스트 연습 > 연습문제 > 정수 제곱근 판별

def solution(n):
    answer = n ** 0.5
    if answer == int(answer):
        return int((answer + 1) ** 2)
    return -1