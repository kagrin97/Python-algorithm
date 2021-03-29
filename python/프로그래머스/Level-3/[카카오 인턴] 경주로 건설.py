from collections import deque
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
    
def racing(n, x, y, board, cost, direction):
    cost[0][0] = 0 # 초기값
    q = deque()
    q.append((0,x,y,0)) # 초기값에서 남쪽, 동쪽 두가지 경우를 구하기위해 
    q.append((0,x,y,1)) # 2가지 값을 넣어줌
    while q:
        curr_cost, x, y, d = q.popleft() # 현재비용, x, y, 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            next_cost = 0
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1:
                continue # 범위를 벗어나거나 막혀있을 경우 통과, 1 = 벽
            if i == d: # 방향이 전과 같으면 직선도로 = 100원
                new_cost = 100
            else: # 방향이 달라졌으므로 직선도로+코너(500원) = 600원
                new_cost = 600
            next_cost = new_cost + curr_cost # 현재 비용과 다음 비용을 더해줌
            if cost[nx][ny] == -1 or cost[nx][ny] >= next_cost: # 한번도 방문하지 않거나, 비용이 더작을경우
                cost[nx][ny] = next_cost # 더 작은 비용으로 교체해줌
                q.append((next_cost, nx, ny, i)) # 현재 비용, x, y, 방향
    
def solution(board):
    n = len(board)
    cost = [[-1] * n for _ in range(n)] # 가격을 넣을 2차배열
    racing(n, 0, 0, board, cost, 0) # 최대 벼열의크기, x, y, board, cost, 방향
    return cost[n-1][n-1]

board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))


