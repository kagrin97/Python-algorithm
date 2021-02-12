import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
time = -1

while q:
    time += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = 1

check = True

for i in graph:
    if 0 in i:
        check = False
        print(-1)
        break

if check:
    print(time)
        