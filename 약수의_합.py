# 코딩테스트 연습 > 연습문제 > 약수의 합

def solution(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        if not result[i] and n % i == 0:
            result[i], result[n // i] = i, n // i
    return sum(result)