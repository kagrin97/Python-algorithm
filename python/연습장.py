from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q.append([x, y])
    check[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[nx][ny] == '.' and check[nx][ny] == 0:
                        check[nx][ny] = check[x][y] + 1
                        q.append([nx, ny])
                    elif board[nx][ny] == 'D':
                        return check[x][y]
                        
            qlen -= 1
        wave()
        
    return "KAKTUS"

def wave():
    qlen = len(q_wave)
    while qlen:
        x, y = q_wave.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == '.':
                    board[nx][ny] = '*'
                    q_wave.append([nx, ny])
        qlen -= 1

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
check = [[0] * C for _ in range(R)]
q, q_wave = deque(), deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            x, y = i, j
            board[x][y] = '.'
        elif board[i][j] == '*':
            q_wave.append([i, j])

wave()
print(bfs(x, y))