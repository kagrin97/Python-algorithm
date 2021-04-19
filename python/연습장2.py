import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[deque() for _ in range(N)] for _ in range(N)]
q = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    board[x-1][y-1].append([m, s, d])
    q.append([x-1, y-1])

for _ in range(K):
    temp = []
    qlen = len(q)
    for _ in range(qlen):
        x, y = q.popleft()
        for _ in range(len(board[x][y])):
            m, s, d = board[x][y].popleft()
            nx = (s * dx[d] + x) % N
            ny = (s * dy[d] + y) % N
            q.append([nx, ny])
            temp.append([nx, ny, m, s, d])
    
    for x, y, m, s, d in temp:
        board[x][y].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                nm, ns, odd, even, flag = 0, 0, 0, 0, 0
                for idx, [m, s, d] in enumerate(board[i][j]):
                    nm += m
                    ns += s
                    if idx == 0:
                        if d % 2 == 0:
                            even = 1
                        else:
                            odd = 1
                    else:
                        if even == 1 and d % 2 == 1:
                            flag = 1
                        elif odd == 1 and d % 2 == 0:
                            flag = 1

                nm //= 5
                ns //= len(board[i][j])
                board[i][j] = deque()
                if nm != 0:
                    for idx in range(4):
                        if flag == 0:
                            nd = 2 * idx
                        else:
                            nd = 2 * idx + 1
                        board[i][j].append([nm, ns, nd])
                    
result = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for m, s, d in board[i][j]:
                result += m
print(result)                    
                    



