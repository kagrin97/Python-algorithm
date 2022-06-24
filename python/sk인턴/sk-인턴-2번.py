def solution(periods, payments, estimates):
    answer = []
    nex_ok = 0 # not vip -> vip!!
    nex_no = 0 # vip -> not nip ㅠㅠ

    for i in range(len(payments)):
        if periods[i] <= 22: #어차피 vip 안됨
            continue

        elif periods[i] == 23: # 다음달에 vip 되면 ok 카운트
            price = payments[i][1:]
            price.append(estimates[i])
            if sum(price) >= 900000:
                nex_ok += 1

        elif periods[i] < 59: # 가입기간 2년~5년 사이 (vip 기준 90만)
            cut_price = sum(payments[i])
            nex_price = payments[i][1:]
            nex_price.append(estimates[i])
            if cut_price >= 900000 and sum(nex_price) < 900000: # vip -> not nip ㅠㅠ
                nex_no += 1
            elif cut_price < 900000 and sum(nex_price) >= 900000: # not vip -> vip!!
                nex_ok += 1

        elif periods[i] == 59: # 다음달 가입기간 5년 (vip 기준 60만)
            cut_price = sum(payments[i])
            nex_price = payments[i][1:]
            nex_price.append(estimates[i])
            if cut_price < 900000 and sum(nex_price) >= 600000: # not vip -> vip!!
                nex_ok += 1
            elif cut_price >= 900000 and sum(nex_price) < 600000: # vip -> not nip ㅠㅠ
                nex_no += 1

        else: # 5년 이상된 장수 고객 (vip 기준 60만)
            cut_price = sum(payments[i])
            nex_price = payments[i][1:]
            nex_price.append(estimates[i])
            if cut_price < 600000 and sum(nex_price) >= 600000: # not vip -> vip!!
                nex_ok += 1
            elif cut_price >= 600000 and sum(nex_price) < 600000: # vip -> not nip ㅠㅠ
                nex_no += 1



    return [nex_ok, nex_no]

periods = [20,23,24]
payments = [각사용자간의 매월납부요금]
estimates = [각사용자간의 다음달 납부예정금]
print(solution(periods, payments, estimates))