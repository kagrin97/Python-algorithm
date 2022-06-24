def solution(n, plans, clients):
    answer = []
    yogm = []

    for i in range(len(plans)):
        p = plans[i].split(" ")

        if len(yogm) < 1: # 요금제에 아무것도 없다면
            p = sorted(map(int,p))
            yogm.append(p)

        else:
            yo = yogm[-1] # 그 전 요금제가 존재하면
            for y in yo:
                if int(y) <= n:
                    p.append(y) # 그 전 요금제 부가서비스를 포함시킴
            p = sorted(map(int,p)) # 데이터 비교를 위한 정렬
            yogm.append(p)

    for i in range(len(clients)):
        c = clients[i].split(" ")
        data = int(c[0]) # 사용자의 필요 data
        service = list(map(int,c[1:])) # 사용자가 필요한 부가서비스
        call = 0 # 사용자가 써도 되는 요금제의 인덱스

        for yo in range(len(yogm)):
            if yogm[yo][-1] >= data: # 사용자가 필요한 data를 충족하는 요금제라면
                flag = True

                for ser in service: # 부가서비스가 포함이 된 요금제인지 비교
                    if ser not in yogm[yo][:-1]:
                        flag = False # 필요 부가서비스가 없으면 flase

                if flag: # 해당 요금제를 검사후 조건이 충족하면 call 갱신
                    call = yo + 1
                    break

        if call == 0: # 충족하는 요금제가 없다면 0 추가
            answer.append(0)
        else:
            answer.append(call)


    return answer

n = 5
plans = ["100 3 1", "500 4", "2000 5"]
clients = ["300 3 5", "1500 1","100 1 3","50 1 2"]

print(solution(n, plans, clients))