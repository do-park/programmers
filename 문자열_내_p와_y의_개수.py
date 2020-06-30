# 코딩테스트 연습 > 연습문제 > 문자열 내 p와 y의 개수

def solution(s):
    p, y = 0, 0
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
    return True if p == y else False