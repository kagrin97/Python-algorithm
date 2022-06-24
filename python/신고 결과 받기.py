def solution(id_list, report, k):
    ans = []
    singo_name = {} # 신고를 한 사람 이름을 담는곳
    singo_cnt = {} # 신고 처리 결과를 받은 횟수를 담는곳
    for i in id_list:
        singo_name[i] = []
        singo_cnt[i] = 0

    for i in report:
        a, b = i.split(" ")
        if a not in singo_name[b]:
            singo_name[b] += [a]

    for i in singo_name:
        if len(singo_name[i]) >= k:
            for s in singo_name[i]:
                singo_cnt[s] += 1

    for i in singo_cnt:
        ans.append(singo_cnt[i])
    return ans

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))