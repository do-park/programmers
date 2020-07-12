# 코딩테스트 연습 > 연습문제 > 시저 암호

def solution(s, n):
    answer = ''
    for i in s:
        temp = ord(i)
        if 65 <= temp <= 90:
            if temp + n > 90:
                answer += chr(temp + n - 26)
            else:
                answer += chr(temp + n)
        elif 97 <= temp <= 122:
            if temp + n > 122:
                answer += chr(temp + n - 26)
            else:
                answer += chr(temp + n)
        else:
            answer += i
    return answer