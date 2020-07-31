# 코딩테스트 연습 > 해시 > 완주하지 못한 선수

def solution(participant, completion):
    temp = 0
    dic = {}
    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))
    for c in completion:
        temp -= int(hash(c))
    answer = dic[temp]
    return answer