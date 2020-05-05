# 2019 KAKAO BLIND RECRUITMENT
# 실패율

def solution(N, stages):
    answer = []
    failed = [0] * (N + 2)
    tried = [0] * (N + 2)
    user = len(stages)
    for i in range(user):
        failed[stages[i]] += 1
        tried[stages[i]] += 1
    for i in range(N, 0, -1):
        tried[i] += tried[i + 1]
    result = []
    for i in range(1, N + 1):
        if tried[i]:
            result.append([i, failed[i]/tried[i]])
        else:
            result.append([i, 0])
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    for i in range(N):
        answer.append(result[i][0])
    return answer