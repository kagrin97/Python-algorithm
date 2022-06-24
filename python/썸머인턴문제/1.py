def solution(code, day, data):
    answer = []
    day += '00'
    for i in range(len(data)):
        p, c, t = data[i].split(' ')
        _, cod = c.split('=')
        _, tim = t.split('=')
        _, pri = p.split('=')
        if code == cod:
            if int(day) <= int(tim) < int(day) + 25:
                answer.append([int(tim), int(pri)])
    s = []
    answer = sorted(answer, key = lambda x:x[0])
    for i in range(len(answer)):
        s.append(answer[i][1])
    return s

code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113",
"price=90 code=012345 time=2019062014",
"price=120 code=987654 time=2019062010",
"price=110 code=012345 time=2019062009",
"price=95 code=012345 time=2019062111"]
print(solution(code, day, data))