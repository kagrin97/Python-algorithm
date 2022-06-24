board = []
for i in range(19):
    board.append(list(map(int, input().split())))

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            focus = board[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus:
                    cnt += 1

                    if cnt == 5:
                        # 육목 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19: # 기준돌 바로전 값이 범위안이고 같은 돌이면 6목이다
                            if board[x - dx[i]][y - dy[i]] == focus:
                                break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19: # 기준돌기준 5번째 돌 다음돌이 범위 안이고 같은돌이면 6목이다
                            if board[nx + dx[i]][ny + dy[i]] == focus:
                                break
                        # 육목이 아니면 성공한거니까 종료
                        print(focus)
                        print(x + 1, y + 1)
                        exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)