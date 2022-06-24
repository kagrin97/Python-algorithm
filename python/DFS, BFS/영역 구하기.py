from collections import deque

M, N, K = map(int, input().split())
location = []
board = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(s1, s2):
  de = deque()
  de.append([s1, s2])
  board[s1][s2] = 1
  cnt = 1

  while de:
    x, y = de.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < M and 0 <= ny < N:
        if board[nx][ny] == 0:
          board[nx][ny] = 1
          cnt += 1
          de.append([nx, ny])
  
  location.append(cnt)

for _ in range(K):
  x1, y1, x2, y2 = list(map(int, input().split()))
  
  for i in range(x1, x2):
    for j in range(y1, y2):
      board[j][i] = 1

for i in range(M):
  for j in range(N):
    if board[i][j] == 0:
      bfs(i, j)
      
print(len(location))
location.sort()
for i in location:
  print(i, end=' ')

  
