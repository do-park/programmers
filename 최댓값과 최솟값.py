def solution(s):
    numbers = list(map(int, s.split()))
    return str(min(numbers)) + ' ' + str(max(numbers))


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
print(solution('-1 -1'))