# 코딩테스트 연습 > 연습문제 > 2016년

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

def solution(a, b):
    days = b
    for i in range(a):
        days += month[i]
    print(days)
    answer = days % 7
    return day[answer]