import sys
from copy import deepcopy
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def up(cleaner, board, tmp_board):
    x, y = cleaner[0] 
    for i in range(2, C):
        tmp_board[x][y+i] = board[x][y+i-1]

    for i in range(x, 0, -1):
        tmp_board[i-1][C-1] = board[i][C-1]

    for i in range(C-1, 0, -1):
        tmp_board[0][i-1] = board[0][i]

    for i in range(1, x+1):
        if i == x+1:
            break
        tmp_board[i][0] = board[i-1][0]

    for i in range(1, x):
        for j in range(1, C-1):
            tmp_board[i][j] = board[i][j]
    return board, tmp_board

def down(cleaner, board, tmp_board):
    x, y = cleaner[1]
    for i in range(2, C):
        tmp_board[x][y+i] = board[x][y+i-1]

    for i in range(x+1, R):
        tmp_board[i][-1] = board[i-1][-1]

    for i in range(C-1, 0, -1):
        tmp_board[-1][i-1] = board[-1][i]

    for i in range(R-1, x, -1):
        tmp_board[i-1][0] = board[i][0]
        

    for i in range(x+1,R-1):
        for j in range(1, C-1):
            tmp_board[i][j] = board[i][j]
    
    return board, tmp_board

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    for j in range(1):
        if board[i][j] == -1:
            cleaner.append((i, j))

for _ in range(T):
    tmp_dust = [[0 for _ in range(C)] for _ in range(R)] 
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and board[i][j] != -1:
                x, y = i, j
                can_move = 0
                dust_val = int(board[i][j] / 5)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    try:
                        if board[nx][ny] != -1 and 0 <= nx < R and 0 <= ny < C:
                            tmp_dust[nx][ny] += dust_val
                            can_move += 1
                    except:
                            pass
                        
                board[x][y] = board[x][y] - (dust_val * can_move)
                tmp_dust[x][y] += board[x][y]
    board = deepcopy(tmp_dust)
    for x, y in cleaner:
        board[x][y] = -1

    tmp_board = [[0 for _ in range(C)] for _ in range(R)]
    up(cleaner, board, tmp_board)
    down(cleaner, board, tmp_board)

    board = tmp_board
    board[x][y] = -1
    board[x-1][y] = -1

result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] != -1 and board[i][j] != 0:
            result += board[i][j]
print(result)




