from copy import deepcopy

sea = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        sea[i][j] = [data[j*2], data[j*2+1]-1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
result = 0 

def turn_left(d):
    return (d + 1) % 8 # 방향 전환

def find_fish(sea, index):
    for i in range(4):
        for j in range(4):
            if sea[i][j][0] == index: # 작은 물고기를 찾으면 위치를 반환
                return (i, j)
    return None # 물고기 못찾으면

def move_all_fishes(sea, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(sea, i)
        if position != None: # 작은 물고기 찾았으면 살행
            x, y = position[0], position[1]
            d = sea[x][y][1] # 작은 물고기 방향 
            for _ in range(8): # 8방향을 다찾음
                nx = x + dx[d]
                ny = y + dy[d]         
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y): # 이동위치에 상어가 없을 경우
                        sea[x][y][1] = d # 현재 위치 물고기와 다음위치 물고기 방향을 서로 바꿔줌
                        sea[x][y], sea[nx][ny] = sea[nx][ny], sea[x][y] # 값도 바꿔줌
                        break
                d = turn_left(d) # 만약 해당 방향에 물고기 없으면 왼쪽으로 45도 돌림

def get_possible_positions(sea, now_x, now_y):
    positions = []
    d = sea[now_x][now_y][1] # 현재 상어 방향
    for _ in range(4): # 끝까지 이동시키기
        now_x += dx[d]
        now_y += dy[d]      
        if 0 <= now_x and now_x < 4 and 0 <= now_y < 4 :         
            if sea[now_x][now_y][0] != -1: # 범위안이고 상어가 아니라면
                positions.append((now_x, now_y)) # 먹을수있는 물고기 위치들 저장
    return positions

def dfs(sea, now_x, now_y, total):
    global result
    sea = deepcopy(sea) 
    total += sea[now_x][now_y][0]
    sea[now_x][now_y][0] = -1 
    move_all_fishes(sea, now_x, now_y) # 물고기 움직이기
    positions = get_possible_positions(sea, now_x, now_y) # 상어 움직이기

    if len(positions) == 0: # 먹을수 있는 물고기가 없으면 최대값 갱신후 종료
        result = max(result, total) 
        return

    for next_x, next_y in positions: # 먹을수있는 모든 물고기에 대해 제귀적으로 실행
        dfs(sea, next_x, next_y, total)

dfs(sea, 0, 0, 0)
print(result)