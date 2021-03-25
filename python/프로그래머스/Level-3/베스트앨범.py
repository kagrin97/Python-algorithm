from collections import defaultdict
def solution(genres, plays):
    answer = []
    gen_dic = defaultdict(int) # defaultdict를 사용하면 if문을써서
    idx_dic = defaultdict(list) # 키값이 있는지 없는지 확인하지 않아도됨

    for i in range(len(genres)):
        gen_dic[genres[i]] += plays[i] # 재생횟수 총합 딕셔너리
        idx_dic[genres[i]].append((plays[i], i)) # 재생횟수와 인덱스 

    gen_dic = sorted(gen_dic.items(), key=lambda x: -x[1])

    for i in idx_dic:
        idx_dic[i] = sorted(idx_dic[i], key=lambda x:-x[0])[:2]
        # 이문제는 최대 2개를 뽑기 때문에 2개만을 잘라준다
    while len(gen_dic) > 0:
        gen_max = gen_dic.pop(0)
        for i in idx_dic: 
            if i == gen_max[0]: # 두개의 dict의 장르가 일치하면
                if len(idx_dic[i]) > 1: # 값이 2개 존재하면
                    answer.append(idx_dic[i][0][1])
                    answer.append(idx_dic[i][1][1])
                    # 2개씩 한번에 넣어줌
                else:
                    answer.append(idx_dic[i][0][1])
                    # 하나만 있으면 하나만 넣음
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

'''
이문제는 함정이 있는데 무조건 장르마다 최대 2개씩만 뽑아야한다
어이없는것은 문제 지문에 이 내용이 없고 output값에서 발견해야됨 ;;
이문제 14번째줄처럼 미리 잘라주면 속도가 더 빨라짐
'''
