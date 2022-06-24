import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

dx8 = ("tmp", 0, -1, -1, -1, 0, 1, 1, 1)    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy8 = ("tmp", -1, -1, 0, 1, 1, 1, 0, -1)

dy4 = (-1, -1, 1, 1)
dx4 = (-1, 1, -1, 1)

clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]  # 구름 좌표
for d, s in moves:
    moved_clouds = []
    for x, y in clouds:
        nx = (x + dx8[d] * s) % N
        ny = (y + dy8[d] * s) % N
        board[nx][ny] += 1
        moved_clouds.append((nx, ny))

    for x, y in moved_clouds:
        cnt = 0
        for d in range(4):
            nx = x + dx4[d]
            ny = y + dy4[d]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                cnt += 1
        board[x][y] += cnt

    new_clouds = []
    for x in range(N):
        for y in range(N):
            if (x, y) not in moved_clouds and board[x][y] > 1:
                board[x][y] -= 2
                new_clouds.append((x, y))
    clouds = new_clouds

water = 0
for i in board:
    water += sum(i)
print(water)