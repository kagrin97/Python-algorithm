def solution(n, t, m, timetable):
    crew = []
    for i in timetable:
        a, b = i.split(':')
        crew.append(int(a)*60 + int(b)) # 크루원들 대기시간을 숫자로 바꿈
    crew.sort()
    
    bus = [(540+t*i, 0, None) for i in range(n)] # (버스출발시간, 인원수, 마지막에탄사람 대기시간)

    bidx, cidx = 0, 0
    while cidx < len(crew): # 모든 크루원들 검사할때까지
        c = crew[cidx] 
        if bidx == len(bus): # 더이상 버스가 없다면 종료
            break
        if c <= bus[bidx][0] and bus[bidx][1] < m: # 버스시간과, 인원수를 고려해 탈수 있따면
            bus_t, cnt, _ = bus[bidx] 
            bus[bidx] = (bus_t, cnt+1, c) # 인원 +1, 마지막사람의 대기시간 갱신
            cidx += 1 # 다음 사람
        else:
            bidx += 1 # 다음 버스 
    
    ret = bus[-1][0] # 만약 마지막 버스에 전부 타지 않았다면, 마지막 버스 시간을 리턴
    if bus[-1][2]: # 버스에 누가 탄 사람이 있고
        if bus[-1][1] == m: # 인원수가 딱 맞으면 마지막에탄 사람을 밀쳐내고 탐 
            ret = bus[-1][2] - 1
    
    return '%02d:%02d' % (ret // 60, ret % 60)

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))