# 2018 KAKAO BLIND RECRUITMENT
# [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = str(bin(arr1[i] | arr2[i]))[2:]
        temp = '0' * (n - len(temp)) + temp
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)
    return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

arr3 = [46, 33, 33, 22, 31, 51]
arr4 = [27, 56, 19, 14, 14, 10]

print(solution(5, arr1, arr2))
print(solution(6, arr3, arr4))
