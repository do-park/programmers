# 2019 카카오 개발자 겨울 인턴십
# 호텔 방 배정

import sys
sys.setrecursionlimit(1500)

def empty(x, rooms):
    if x not in rooms:
        rooms[x] = x + 1
        return x
    p = empty(rooms[x], rooms)
    rooms[x] = p + 1
    return p

def solution(k, room_number):
    answer = []
    rooms = dict()
    for i in room_number:
        book = empty(i, rooms)
        answer.append(book)
    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))