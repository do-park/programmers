# 코딩테스트 연습 > 해시 > 위장
from collections import defaultdict

def solution(clothes):
    name, category = 0, 1
    categories = defaultdict(int)
    for cloth in clothes:
        categories[cloth[category]] += 1
    answer = 1
    for quantity in categories.values():
        answer *= (quantity + 1)
    return answer - 1


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))