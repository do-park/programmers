# 코딩테스트 연습 > 정렬 > 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*4, reverse=True)
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9, 0]))