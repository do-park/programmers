# 코딩테스트 연습 > 스택/큐 > 프린터

def solution(priorities, location):
    queue = [(idx, priority) for idx, priority in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))        # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5