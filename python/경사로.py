def check(road):
    global count 
    for i in range(n):
        cur_h = road[i][0] # 초기높이
        flat = 1 # 평평한곳이 얼마나 연속됬는지
        for j in range(1,n):
            if road[i][j] == cur_h: # 현재높이와 다음높이가 같다면
                flat += 1 # 평평카운트 증가
            elif road[i][j] == cur_h+1 and flat >= 0: #다음높이가 더높을때
                if flat >= l: # 경사로를 지을수있을만큼 평평길이가 가능할때
                    flat = 1 
                    cur_h = road[i][j]
                else:
                    break # 공간이 부족하면 종료
            elif road[i][j] == cur_h-1 and flat >= 0: # 다음높이가 낮을때
                flat = - l + 1 # 평평을 -로 바꿔 미래지을 경사로 값을 미리 지불
                cur_h = road[i][j]
            else: # 높이차가 2이상일떄
                break
        else: 
            if flat >= 0: # 미리 지불했고 경사로 설치를 했을때
                count += 1

n, l = map(int, input().split())
road_row = [list(map(int, input().split())) for _ in range(n)]
road_col = [] # 세로값을 구하기위해 세로로 만들어줌
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(road_row[j][i])
    road_col.append(tmp)
count = 0

check(road_row)
check(road_col)
print(count)
