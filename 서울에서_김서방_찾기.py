# 코딩테스트 연습 > 연습문제 > 서울에서 김서방 찾기

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return f'김서방은 {i}에 있다'