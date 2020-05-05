# 2018 KAKAO BLIND RECRUITMENT
# 프렌즈4블록

def solution(M, N, board):
    answer = 0
    new = [[board[m][n] for m in reversed(range(M))] for n in range(N)]
    while True:
        check = set()
        for n in range(N - 1):
            for m in range(M - 1):
                if new[n][m] != 0:
                    temp = new[n][m]
                    if temp == new[n + 1][m] and temp == new[n][m + 1] and temp == new[n + 1][m + 1]:
                        check.add((n, m))
                        check.add((n, m + 1))
                        check.add((n + 1, m))
                        check.add((n + 1, m + 1))
        if not check:
            break
        check = list(check)
        check = sorted(check, key=lambda x: (-x[0], -x[1]))
        answer += len(check)
        for (y, x) in check:
            new[y].pop(x)
        print(new)
        for n in range(N):
            new[n] = new[n] + [0] * (M - len(new[n]))
        print(new)
    return answer