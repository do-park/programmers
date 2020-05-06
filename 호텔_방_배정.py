# 2019 카카오 개발자 겨울 인턴십
# 호텔 방 배정
# 정확성: 78.8 , 효율성: 0.0, 합계 78.8/100

def solution(k, room_number):
    answer = []
    hotel = [False] * (k + 1)
    for room in room_number:
        if not hotel[room]:
            hotel[room] = True
            answer.append(room)
        else:
            i = 1
            while True:
                if not hotel[room + i]:
                    hotel[room + i] = True
                    answer.append(room + i)
                    break
                else:
                    i += 1
    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))