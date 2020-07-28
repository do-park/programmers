# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 예산

def solution(d, budget):
    answer = len(d)
    total = sum(d)
    if total <= budget:
        return answer
    else:
        d = sorted(d, reverse=True)
        for i in d:
            answer -= 1
            total -= i
            if total <= budget:
                return answer