from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(x, y):
    board[x][y] = 0
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append([nx, ny])

while True:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0:
                bfs(i, j)
                cnt += 1
    print(cnt)
