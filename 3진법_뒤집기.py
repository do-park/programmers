# 월간 코드 챌린지 시즌1
# 3진법 뒤집기

def solution(n):
    result = []
    while n:
        result.append(n % 3)
        n = n // 3
    result.reverse()
    answer = 0
    for idx, value in enumerate(result):
        answer += value * (3 ** idx)
    return answer