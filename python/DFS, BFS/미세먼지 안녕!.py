import sys
from copy import deepcopy
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def up(cleaner, board, tmp_board): # 오른쪽, 위, 왼쪽, 아래로 먼지를 날려줌
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

def down(cleaner, board, tmp_board): # 오른쪽, 아래, 왼쪽, 위로 먼지를 날려줌
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

R, C, T = map(int, input().split()) # R = X좌표, C = Y좌표, T는 시간이다
board = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    for j in range(1):
        if board[i][j] == -1:
            cleaner.append((i, j)) # 공기청정기 위치를 저장

for _ in range(T): # 시간만큼 작동
    tmp_dust = [[0 for _ in range(C)] for _ in range(R)] # 임시 먼지표
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and board[i][j] != -1: # 먼지가 있으면
                x, y = i, j
                can_move = 0 # 먼지가 이동가능 위치의 수
                dust_val = int(board[i][j] / 5) # 퍼지는 먼지의 값
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    try:
                        if board[nx][ny] != -1 and 0 <= nx < R and 0 <= ny < C:
                            tmp_dust[nx][ny] += dust_val # 먼지가 표를 벗어나지 않으면 먼지 퍼트림
                            can_move += 1 # 이동한 수
                    except:
                            pass
                        
                board[x][y] = board[x][y] - (dust_val * can_move) # 먼지의 진원지가 옅어짐(퍼졌기 때문에)
                tmp_dust[x][y] += board[x][y]
    board = deepcopy(tmp_dust)
    for x, y in cleaner:
        board[x][y] = -1 # 청정기위치 다시 정립

    tmp_board = [[0 for _ in range(C)] for _ in range(R)]
    up(cleaner, board, tmp_board)
    down(cleaner, board, tmp_board)

    board = tmp_board
    board[x][y] = -1 # 공기청정기위치 다시 정립
    board[x-1][y] = -1

result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] != -1 and board[i][j] != 0:
            result += board[i][j] # 미세먼지 값들을 모두 더해줌
print(result)

''' 
위 문제는 시뮬레이션 문제로 원래 표와 먼지를 퍼뜨리는 표, 먼지를 날려보내는 표 따로따로
만들어 줘야 하는 문제이다
''' 

