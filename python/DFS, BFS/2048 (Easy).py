from copy import deepcopy
from collections import deque

def move(board, d):
    can_merged = [[True] * n for _ in range(n)]
    # 병합이 될수있는지 여부를 알려주는 배열

    # 상하좌우에 따라 반복문의 진행 방향이 다르다
    if d in [0,3]: # 위, 왼쪽으로 이동하는 경우
        start, end, step = 0, n, 1
    else: # 오른쪽, 아래로 이동하는 경우
        start, end, step = n-1, -1, -1

    for i in range(start, end, step):
        for j in range(start, end, step):
            if board[i][j] == 0: # 현재값이 0이면 지나감
                continue

            x, y = i, j
            value = board[x][y]
            board[x][y] = 0 # 현재값 비워줌
            nx, ny = x + dx[d], y + dy[d] # 다음 이동 경로

            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break # 범위를 벗어나면 종료
                    
                if board[nx][ny] == 0: # 다음 값이 0이라면
                    x, y = nx, ny 
                    nx, ny = x + dx[d], y + dy[d]
                
                elif board[nx][ny] == value and can_merged[nx][ny]: # 다음 값과 현재값이 같고 병합이 가능하면
                    x, y = nx, ny
                    can_merged[x][y] = False # 한번 병합했으니 2번은 병합 못하게 해줌
                    break
                else: # 다음 좌표가 같은값도아니고 병합도 안되면 종료
                    break
            board[x][y] = board[x][y] + value # 해당좌표 값을 개신
    return board

def bfs(board):
    q = deque([board])
    max_value = -1 # 각판마다 최대값을 저장하는 곳
    step = 0 # 5번 실행을 체크

    while q:
        size = len(q)
        for _ in range(size):
            board = q.popleft()
            for d in range(4):
                next_board = move(deepcopy(board), d)
                q.append(next_board)

                for i in range(n):
                    for j in range(n):
                        if next_board[i][j] > max_value:
                            max_value = next_board[i][j]
        step += 1

        if step == 5:
            return max_value

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(bfs(board)) 

            

