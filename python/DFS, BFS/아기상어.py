from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, weight, time, eat):
    q, can_eat = deque(), []
    q.append([x, y])
    fish_dis = [[-1] * n for _ in range(n)] # 거리를 재기위한 2차원배열
    fish_dis[x][y] = time # 현재까지걸린 시간 저장
    while q:
        qlen = len(q) 
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n: # 범위를 벗어나지 않고
                    if fish_dis[nx][ny] == -1: # 방문한적이 없으며
                        if sea[nx][ny] == 0 or sea[nx][ny] == weight: # 아무것도없거나 무게가 같을때
                            fish_dis[nx][ny] = fish_dis[x][y] + 1 # 통과하기위해 이동거리 갱신
                            q.append([nx, ny]) # 이동한 위치 저장
                        elif 0 < sea[nx][ny] < weight: # 먹을수 있는 물고기 라면
                            can_eat.append([nx, ny]) # 먹을수있는 물고기 리스트에 저장
            qlen -= 1

        if can_eat:
            nx, ny = min(can_eat) # 가장위쪽 왼쪽부터 먹기위해 min
            eat += 1 # 먹음
            if eat == weight: # 먹은무게와 무게가 같아지면
                eat = 0 # 초괴화
                weight += 1 # 무게증가
            sea[nx][ny] = 0 # 먹힌 물고기 삭제
            return nx, ny, weight, fish_dis[x][y]+1, eat # fish_dis[x][y]+1는 이떄까지 걸린 시간이다 

    print(time) # return이 되지않으면 실행된다 즉 먹을수있는 물고기가 없을때 걸린 시간을 출력
    sys.exit() # 그리고 종료
    
n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9: # 아기상어위치와 아기상어의 위치를 없앰
            x, y = i, j
            sea[i][j] = 0
weight, time, eat = 2, 0, 0 # 무게, 걸린시간, 먹은무게
while True:
    x, y, weight, time, eat = bfs(x, y, weight, time, eat)