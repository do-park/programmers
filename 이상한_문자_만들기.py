# 코딩테스트 연습 > 연습문제 > 이상한 문자 만들기

def solution(s):
    L = len(s)
    answer = ''
    i = 0
    for l in range(L):
        if s[l] == ' ':
            i = 0
            answer += ' '
        elif i & 1:
            answer += s[l].lower()
            i += 1
        else:
            answer += s[l].upper()
            i += 1
    return answer