# 2019 카카오 개발자 겨울 인턴십
# 튜플
import operator

def solution(s):
    answer = []
    numbers = s.replace('{', "").replace('}','').split(',')
    tuples = dict()
    for number in numbers:
        if number in tuples:
            tuples[number] += 1
        else:
            tuples[number] = 1
    tuples = sorted(tuples.items(), key=operator.itemgetter(1), reverse=True)
    for key, value in tuples:
        answer.append(int(key))
    return answer