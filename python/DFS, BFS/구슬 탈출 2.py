from collections import deque
N, M = map(int, input().split())
B = [list(input().rstrip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)] 
# 빨공x,y 파공x,y정보를 2차원배열 *2 개로 나타냄

def move(x, y, dx, dy):
    cnt = 0
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def position():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            elif B[i][j] == 'B':
                bx, by = i, j
    queue.append((rx, ry, bx, by, 1)) 
    visited[rx][ry][bx][by] = True # 빨공, 파공의 위치정보를 2차원 *2 개씩 위치를 나타냄

def solution():
    position()
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10: # 10번을 넘으면 -1을 출력
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if B[nbx][nby] != 'O':
                if B[nrx][nry] == 'O':
                    print(depth) # 10번안에 도착하면 움직인 횟수 출력
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)

solution()

'''
구슬 탈출1과 매우 흡사하지만 움직인 횟수가 10번 이하이고 구멍이 도착했으면
움직인 횟수를 출력후 종료한다
'''

