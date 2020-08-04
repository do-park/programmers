# 코딩테스트 연습 > 연습문제 > 콜라스 추측

def solution(num, cnt=0):
    if num == 1 or cnt > 500:
        return cnt if cnt < 500 else -1
    if num & 1:
        return solution(num * 3 + 1, cnt + 1)
    else:
        return solution(num // 2, cnt + 1)