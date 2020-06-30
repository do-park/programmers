# 코딩테스트 연습 > 연습문제 > 소수 찾기

def solution(n):
    if n <= 1:
        return 0
    numbers = [True] * (n + 1)
    numbers[0], numbers[1] = False, False
    for i in range(2, n + 1):
        if numbers[i]:
            for j in range(2, n + 1):
                if i * j <= n:
                    numbers[i * j] = False
                else:
                    break
    return numbers.count(True)