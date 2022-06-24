import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    check[x][y] = -1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == board[x][y] and check[nx][ny] == 0:
                    q.append([nx, ny])
                    check[nx][ny] = -1

n = int(input())
board = [list(map(str, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = "G"

check = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)


