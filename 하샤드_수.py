# 코딩테스트 연습 > 연습문제 > 하샤드 수

def solution(x):
    return not(x % sum([int(i) for i in str(x)]))