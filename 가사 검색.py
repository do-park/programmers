# 2020 KAKAO BLIND RECRUITMENT
# 가사 검색
# 정확도 18/18(25.0), 효율성 2/5(30.0), 합계: 55/100

def solution(words, queries):
    LQ = len(queries)
    answer = [0] * LQ
    for q in range(LQ):
        query = queries[q]
        lq = len(query)
        for w in words:
            if lq == len(w):
                for i in range(lq):
                    if query[i] == '?':
                        continue
                    if query[i] != w[i]:
                        break
                else:
                    answer[q] += 1
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))