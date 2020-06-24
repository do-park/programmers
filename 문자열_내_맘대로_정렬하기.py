# 코딩테스트 연습 > 연습문제 > 문자열 내 맘대로 정렬하기

def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda x: x[n])
    return answer