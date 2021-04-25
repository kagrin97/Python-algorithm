from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(x, y, t_x, t_y):
    q = deque()
    q.append([x, y])
    board = [[0] * n for _ in range(n)]
    board[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == t_x and y == t_y:
            return board[t_x][t_y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                q.append([nx, ny])
                board[nx][ny] = board[x][y] + 1

t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    t_x, t_y = map(int, input().split())
    print(bfs(x, y, t_x, t_y))