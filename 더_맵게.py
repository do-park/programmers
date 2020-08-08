# 코딩테스트 연습 > 힙(Heap) > 더 맵게

from heapq import heappush, heappop

def solution(scoville, K):
    q = []
    for s in scoville:
        heappush(q, s)
    answer = 0
    while True:
        x = heappop(q)
        if x >= K:
            return answer
        if q:
            y = heappop(q)
            heappush(q, x + 2 * y)
            answer += 1
        else:
            return -1