# 코딩테스트 연습 > 연습문제 > 정수 내림차순으로 배치하기

def solution(n):
    numbers = [0] * 10
    while n > 0:
        numbers[n % 10] += 1
        n //= 10
    answer = 0
    for i in range(9, -1, -1):
        for j in range(numbers[i]):
            answer = answer * 10 + i
    return answer