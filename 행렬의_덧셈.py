# 코딩테스트 연습 > 연습문제 > 행렬의 덧셈

def solution(arr1, arr2):
    col = len(arr1)
    row = len(arr1[0])
    answer = [[0] * row for _ in range(col)]
    for c in range(col):
        for r in range(row):
            answer[c][r] = arr1[c][r] + arr2[c][r]
    return answer