import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, L, R = map(int, input().split())

board = list()
for i in range(N):
    board.append(list(map(int, input().split())))

def bfs(i, j):
    q = deque()
    q.append((i, j))        # 이런식으로 넣어줘야 unpack에러가 안남
    visited[i][j] = True
    union = [(i, j)]        # 국가 위치
    human_cnt = board[i][j]     # 연결된 나라 총인구

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(board[nx][ny] - board[x][y]) <= R:  # 두나라 인구수 차이가 L이상 R이하일떄
                    union.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    human_cnt += board[nx][ny]

    for x, y in union:
        board[x][y] = human_cnt // len(union)   # 국가마다 인구를 나눠서 넣어줌

    return len(union)   # 연결된 국가 숫자

day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j) > 1:   # 연결된 국가가 2개이상일떄
                    flag = True
    if not flag:    # 연결된국가가 없으면 종료
        break
    day += 1

print(day)

# 이문제는 쉬운문제인데 너무 어렵게 생각해서 정답답을 찾아본 문제이다