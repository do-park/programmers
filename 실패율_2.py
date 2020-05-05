# 2019 KAKAO BLIND RECRUITMENT
# 실패율

def solution(N, stages):
    failed = [0] * (N + 2)
    tried = len(stages)
    for i in range(tried):
        failed[stages[i]] += 1
    result = {}
    for i in range(1, N + 1):
        if tried:
            result[i] = failed[i] / tried
            tried -= failed[i]
        else:
            result[i] = 0
    print(result)
    return sorted(result, key=lambda x: result[x], reverse=True)