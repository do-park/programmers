# 코딩테스트 연습 > 완전탐색 > 카펫

def solution(brown, yellow):
    total = brown + yellow
    for row in range(1, total):
        col = total // row
        if (col - 2) * (row - 2) == yellow:
            return [col, row]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))