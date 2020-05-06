# 2018 KAKAO BLIND RECRUITMENT
# [1차] 캐시

from collections import deque

def solution(cacheSize, cities):
    Q = deque(maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.upper()
        if city in Q:
            answer += 1
            Q.remove(city)
            Q.append(city)
        else:
            answer += 5
            Q.append(city)
    return answer