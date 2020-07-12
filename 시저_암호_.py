# 코딩테스트 연습 > 연습문제 > 시저 암호
def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i.islower():
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += i
    return answer