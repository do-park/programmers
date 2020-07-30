# 코딩테스트 연습 > 연습문제 > 정수 내림차순으로 배치하기

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))