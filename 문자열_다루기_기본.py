# 코딩테스트 연습 > 연습문제 > 문자열 다루기 기본

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdecimal():
            return True
    return False