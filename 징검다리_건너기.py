# 2019 카카오 개발자 겨울 인턴십
# 징검다리 건너기
# 정확성 61.5(24/25), 효율성 35.9(10/10), 합계 97.4

def can(stones, k, mid):
    count = 0
    for stone in stones:
        if stone < mid:
            count += 1
        else:
            count = 0
        if count >= k:
            return False
    return True

def solution(stones, k):
    left = 1
    right = max(stones)
    while left < (right - 1):
        mid = (left + right) // 2
        if can(stones, k, mid):
            left = mid
        else:
            right = mid
    return left


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
result = 3
print(solution(stones, k))
