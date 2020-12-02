from collections import defaultdict

def solution(genres, plays):
    total_dict = defaultdict(int)
    sub_dict = defaultdict(list)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        total_dict[genre] += play
        sub_dict[genre].append((idx, play))
    total_dict = sorted(total_dict.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for key in total_dict:
        play_list = sub_dict[key[0]]
        play_list = sorted(play_list, key=lambda x: (-x[1], x[0]))
        answer.append(play_list[0][0])
        if len(play_list) >= 2:
            answer.append(play_list[1][0])
    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop', 'music'], [500,  600, 140, 800, 2500, 1]))