def solution(land):
    N = len(land)
    dp = [[0, 0, 0, 0] for _ in range(N)]
    dp[0] = land[0]
    for row in range(1, N):
        dp[row][0] = max(dp[row-1][1], dp[row-1][2], dp[row-1][3]) + land[row][0]
        dp[row][1] = max(dp[row-1][0], dp[row-1][2], dp[row-1][3]) + land[row][1]
        dp[row][2] = max(dp[row-1][0], dp[row-1][1], dp[row-1][3]) + land[row][2]
        dp[row][3] = max(dp[row-1][0], dp[row-1][1], dp[row-1][2]) + land[row][3]
    return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))