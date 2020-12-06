# 코딩테스트 연습 > 스택/큐 > 프린터
from collections import deque


def solution(priorities, location):
    q = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    order = 0
    max_priority = max(q)
    while q:
        priority, idx = q.popleft()
        if max_priority[0] == priority:
            order += 1
            if idx == location:
                return order
            max_priority = max(q)
        else:
            q.append((priority, idx))


print(solution([2, 1, 3, 2], 2))        # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5