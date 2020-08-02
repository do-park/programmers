# 코딩테스트 연습 > 연습문제 > 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    a, b = min(n, m), max(n, m)
    while a > 0:
        a, b =  b % a, a
    answer.append(b)
    answer.append(n * m // b)
    return answer