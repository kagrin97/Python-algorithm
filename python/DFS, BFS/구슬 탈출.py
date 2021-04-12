from collections import deque
N, M = map(int, input().split())
B = [list(input().rstrip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# 빨공x,y 파공x,y정보를 2차원배열 *2 개로 나타냄 즉 4차원 배열

def move(x, y, dx, dy):
    cnt = 0 # cnt는 이동한 거리
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O': # 다음 위치가 벽x,구멍x 일떄까지
        x += dx # 계속 굴려줌
        y += dy
        cnt += 1 # 이동거리 갱신
    return x, y, cnt

def position():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R': # 빨공 찾으면 rx,ry에 위치 정보 추가
                rx, ry = i, j
            elif B[i][j] == 'B': # 파공 찾으면 bx,by에 위치 정보 추가
                bx, by = i, j
    queue.append((rx, ry, bx, by, 1)) # 1은 깊이로 움직이는 횟수를 의미
    visited[rx][ry][bx][by] = True # 빨공, 파공의 위치정보를 2차원 *2 개씩 위치를 나타냄

def solution():
    position() # 초기값 설정
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10: # 10번이상 움직이면 종료
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i]) 
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if B[nbx][nby] != 'O': # 파공이 구멍을 만나지 않고
                if B[nrx][nry] == 'O': # 빨공이 구멍을 만났으면 1출력
                    print(1)
                    return
                if nrx == nbx and nry == nby: # 파공, 빨공이 겹치면
                    if rcnt > bcnt: # 빨공 이동거리가 더 멀면 빨공이 더멀리 있었기때문에
                        nrx -= dx[i] # 빨공을 한칸 뒤로 보냄
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]: # 4차원 배열에 방문기록 작성
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth+1)) # 움직인 횟수 1추가
    print(0) # 10번안에 못 도착하면 0 출력

solution()


