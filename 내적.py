# 월간 코드 챌린지 시즌1 > 내적

def solution(A, B):
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer