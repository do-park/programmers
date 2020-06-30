# 코딩테스트 연습 > 연습문제 > 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    temp = arr[0]
    for a in arr:
        if a != temp:
            answer.append(a)
        temp = a
    return answer