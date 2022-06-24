from itertools import permutations
def solution(k, dungeons):
    ans = 0
    dungeons_P = list(permutations(dungeons, len(dungeons))) # 클리어순서 순열
    for dungeon in dungeons_P:
        cur_k = int(k) # 현재 피로도
        clear_cnt = 0 # 완료한 던전수
        for ieast_k, need_k in dungeon: # 최소피로도, 소모필요도
            if ieast_k <= cur_k:
                cur_k -= need_k
                clear_cnt += 1
            else:                   # 최소피로도를 못넘으면 거기서 끝
                if ans < clear_cnt: # 현재 완료던전수 저장
                    ans = clear_cnt
                    break
        if ans < clear_cnt:
            ans = clear_cnt
    return ans

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))