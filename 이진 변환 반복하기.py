# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 이진 변환 반복하기

def solution(s):
    conversion, deleted_zeros = 0, 0
    while s != '1':
        deleted_zeros += s.count('0')
        s = bin(s.count('1'))[2:]
        conversion += 1
    return [conversion, deleted_zeros]

print(solution('110010101001'))
print(solution('01110'))
print(solution('1111111'))