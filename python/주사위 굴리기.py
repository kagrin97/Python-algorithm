import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0 for _ in range(6)] # 0은 윗면 5는 바닥면

for i in range(k):
    dir = order[i] - 1 # 명령어를 dx에 적용시키기 위해 1씩빼줌
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    if dir == 0: # 주사위가 동쪽으로 이동할때 주사위 값들을 변경해줌 (직접 상자에 그려보고 이해함)
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if a[nx][ny] == 0: # 도착칸에 값이 0이면 주사위 밑면 값을 넣어줌
        a[nx][ny] = dice[5]
    else:
        dice[5] = a[nx][ny] # 칸에 값이 있으면 주사위 밑면에 복사후 칸을 0으로 갱신
        a[nx][ny] = 0

    x, y = nx, ny
    print(dice[0]) # 주사위 윗면 값 출력
