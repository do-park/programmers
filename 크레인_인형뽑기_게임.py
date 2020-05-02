# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        move -= 1
        N = len(board)
        for i in range(N):
            if board[i][move]:
                crane = board[i][move]
                board[i][move] = 0
                break
        if stack and stack[-1] == crane:
            stack.pop()
            answer += 2
        elif crane:
            stack.append(crane)
        crane = 0
    return answer