R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
dx,dy = [-1,1,0,0], [0,0,-1,1]

new_board = [['.'] * C for _ in range(R)]
idx = []                # 살아남은 섬 주소
for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            see_cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[nx][ny] == '.':
                        see_cnt += 1        # 4방향중 바다가 있으면 cnt +1
                else:
                    see_cnt += 1            # 범위를 벗어난곳은 바다이기 때문에 cnt +1
            if see_cnt < 3:                 # 주위 바다가 2면 이하이면
                new_board[i][j] = 'X'       # 새로운 지도를 만들어줌
                idx.append([i, j])          # 주소 추가

idx = sorted(idx, key=lambda x:x[1])        # y의 최소,최대값을 구하기우함
start_y, end_y = idx[0][1], idx[-1][1]
idx = sorted(idx, key=lambda x:x[0])        # x의 최소,최대값을 구하기위함
start_x, end_x = idx[0][0], idx[-1][0]

for i in range(start_x, end_x+1):           # x의최소부터 y의 최대까지 출력해줌
    for j in range(start_y, end_y+1):
        print(new_board[i][j], end="")
    print()
