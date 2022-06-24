def checktr(time, lin):
    cnt = 0
    start = time
    end = time + 1000 # 겹치는 구간은  넓이는 1초씩이기때문에 1초 추가
    for i in lin:
        if i[1] >= start and i[0] < end: # 시작과 끝을 기준으로 포함이 되면
            cnt += 1 
    return cnt

def solution(lines):
    lin = []
    result = 1 # 최소 한개씩은 실행 했기때문에 기본값
    for i in lines:
        _, t, s = i.split()
        t = t.split(':')
        s = float(s.replace('s','')) * 1000 # 1초 = 1000밀리초, s삭제
        end = (int(t[0]) * 3600 + int(t[1]) * 60 + float(t[2])) * 1000 # 전체 시간을 밀리초로 바꿈
        start = end - s + 1 # 시작시간은 +1을 포함한다
        lin.append([start, end]) # 밀리초(시작시간, 끝난시간)

    for i in lin:
        result = max(result, checktr(i[0], lin), checktr(i[1], lin)) 
    return result

lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print(solution(lines))

'''
어려운 문제
'''
