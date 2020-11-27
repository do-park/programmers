# 코딩테스트 연습 > 동적계획법(Dynamic Programming) > 정수 삼각형

def solution(triangle):
    rows = len(triangle)
    for row in range(1, rows):
        for col in range(row + 1):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]
            elif col == row:
                triangle[row][col] += triangle[row-1][col-1]
            else:
                triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])
    return max(triangle[-1])



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))