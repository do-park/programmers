# 코딩테스트 연습 > 스택/큐 > 기능개발

from collections import deque
from math import ceil

def solution(progresses, speeds):
    completes = deque()
    for progress, speed in zip(progresses, speeds):
        completes.append(ceil((100 - progress) / speed))
    print(completes)
    answer = []
    deploy, count = completes.popleft(), 1
    while completes:
        complete = completes.popleft()
        if complete <= deploy:
            count += 1
        else:
            answer.append(count)
            deploy, count = complete, 1
    answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))     # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))   # [1, 3, 2]