# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 영어 끝말잇기

def solution(n, words):
    cnt = len(words)
    done = {words[0]}
    for turn in range(1, cnt):
        if words[turn] in done:
            return [turn % n + 1, turn // n + 1]
        if words[turn - 1][-1] != words[turn][0]:
            return [turn % n + 1, turn // n + 1]
        done.add(words[turn])
    return [0, 0]


print(solution(3, 	['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, 	['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))