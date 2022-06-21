import math

def pay(time, fees):
    if time <= fees[0]:  # 기본시간을 채우지 못했다면 기본요금을 리턴
        return fees[1]
    p = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]  # 이 공식은 문제에서 알려줌
    return p

def solution(fees, records):
    ans = []
    log = {}  # {차번호: [출입시간, 나간시간, ...., ..]}

    for r in records:
        t, num, act = r.split(' ')
        h, m = map(int, t.split(":"))
        time = (h * 60) + m
        if num in log:
            log[num].extend([time])
        else:
            log[num] = [time]

    for key in log:
        if len(log[key]) % 2 != 0:  # 홀수라는 뜻은 마지막으로 나간시간이 없다는 뜻
            log[key].extend([1439])  # 23시59분 값을 넣어줌

        if len(log[key]) == 2:  # 처음부터 길이가 2라면은 차량이 한대만 통행했다는 뜻
            log[key] = log[key][1] - log[key][0]

        elif len(log[key]) >= 4:  # 여러차량이 통행을 했으면 각차량의 out - in = 시간을 계산
            tmp = []
            for i in range(0, len(log[key]), 2):
                tmp.append(log[key][i + 1] - log[key][i])
            log[key] = tmp

        if isinstance(log[key], list):  # item의 값이 리스트라면 여러번 출입을 했다는뜻
            log[key] = sum(log[key])
    time_log = sorted(log.items(), key=lambda x: int(x[0]))  # 차량번호를 오름차순을 기준으로 계산해주길원함

    for _, time in time_log:
        ans.append(pay(time, fees))
    return ans

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))