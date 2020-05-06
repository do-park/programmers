# 2018 KAKAO BLIND RECRUITMENT
# [3차] 압축

dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
        'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
        'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
def solution(msg):
    answer = []
    num = 27
    while msg:
        L = len(msg)
        for i in range(L, 0, -1):
            w = msg[0:i]
            if w in dict:
                answer.append(dict[w])
                if i != L:
                    dict[w + msg[i]] = num
                    num += 1
                msg = msg[i:]
                break
    return answer