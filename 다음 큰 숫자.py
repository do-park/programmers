# 코디엩스트 연습 > 연습문제 > 다음 큰 숫자

def solution(n):
    ones, answer = bin(n).count('1'), n + 1
    while True:
        if bin(answer).count('1') == ones:
            return answer
        answer += 1


print(solution(78))     # 83
print(solution(15))     # 23