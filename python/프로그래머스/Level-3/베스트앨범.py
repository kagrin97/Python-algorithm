def solution(genres, plays):
    ans = []
    play_cnt = []
    music = {}
    for i in range(len(plays)):
        if genres[i] in music:
            music[genres[i]] += [[i, plays[i]]]  # 고유번호 i와 플레이 횟수를 넣어줌
        else:
            music[genres[i]] = [[i, plays[i]]]

    for gen in music:
        tmp_cnt = 0
        for info in music[gen]:  # 해당 장르곡들의 횟수들을 더해줌
            tmp_cnt += info[1]
        play_cnt.append([gen, tmp_cnt])  # 장르와 총 횟수를 넣어줌

    play_cnt = sorted(play_cnt, key=lambda x: x[1], reverse=True)  # 장르별 플레이횟수 정렬

    for g, _ in play_cnt:
        tmp_g = sorted(music[g], key=lambda x: int(x[1]), reverse=True)  # 해당장르 내에서 많이 재생된노래 정렬

        if len(tmp_g) == 1:  # 해당장르노래가 1개만있을경우 하나만 넣음
            ans.append(tmp_g[0][0])
        else:
            for i in range(2):  # 2곡이상 있으면 2곡만 넣어줌
                ans.append(tmp_g[i][0])

    return ans

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

'''
2022 06 21에 다시풀음 
이번에는 혼자서 풀었당
'''
