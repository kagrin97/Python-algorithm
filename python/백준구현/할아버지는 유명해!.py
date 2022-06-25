while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:                           # 0,0을 만나면 종료
      break
    score = [list(map(int, input().split())) for i in range(N)]
    log = dict()
    for scor in score:
        for s in scor:
            if s in log:
                log[s] += 1
            else:
                log[s] = 0

    log = sorted(log.items(), key=lambda x:-x[1])   # 점수 내림차순 정렬
    second_score = log[1][1]                        # 2등 점수를 가져옴
    ans = []
    for i in log:
        if i[1] == second_score:                    # 2등 점수랑 일치하면 번호 넣어줌
            ans.append(i[0])
    ans.sort()
    print(*ans)


