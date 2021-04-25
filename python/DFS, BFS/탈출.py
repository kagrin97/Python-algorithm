from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q.append([x, y])
    check[x][y] = 1 # 고슴되치 이동
    while q:
        qlen = len(q) # 고슴도치가 딱한번씩만 움직이기 위해 len
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[nx][ny] == '.' and check[nx][ny] == 0: # 방문한적없고 빈공간이면 이동
                        check[nx][ny] = check[x][y] + 1 # 이동거리 계산
                        q.append([nx, ny])
                    elif board[nx][ny] == 'D': # 대피소를 만나면 이동거리 출력
                        return check[x][y]
                        
            qlen -= 1
        wave() # 대피소를 고슴도치가 못만나면 파도를 한번더 침

    return "KAKTUS" # q가 비었다는 것은 고슴도치가 모든곳을 이동해도 대피소를 못갔다는 의미이기때문에 kaktus 출력

def wave():
    qlen = len(q_wave) # while q를 사용하지 않는 이유는 파도가 딱한번씩만 쳐야하기 때문이다
    while qlen: # q에 들은 바닷물 수만큼만 실행됨
        x, y = q_wave.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == '.': # 빈공간이면 바닷물을 넣음
                    board[nx][ny] = '*'
                    q_wave.append([nx, ny]) 
        qlen -= 1 # len을 사용하기위한 -=1

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
check = [[0] * C for _ in range(R)]
q, q_wave = deque(), deque() # q=고슴도치 위치, q_wave=파도위치

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S': # 고슴도치 위치
            x, y = i, j 
            board[x][y] = '.' # 빈공간으로 바꿔줌
        elif board[i][j] == '*': 
            q_wave.append([i, j])

wave() # 바닷물 먼저 깔림
print(bfs(x, y)) # 그리고 고슴도치 이동