from collections import deque
n = int(input())
target = int(input())
board_num = [i for i in range(1, n*n+1)] # 1~n*n 만큼 수가들어간 리스트
board = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append([0, 0, 0]) # x, y, 방향
board[0][0] = board_num.pop() # 초기값 넣음

while board_num:
    x, y, d = q.popleft()
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0: # 범위 안이고 한번도 안가본 곳이면
        board[nx][ny] = board_num.pop()
        q.append([nx, ny, d])
    else: # 범위 밖을 벗어 나기 때문에 방향을 바꿔준다
        if d == 0: 
            q.append([x, y, 2])
        elif d == 1:
            q.append([x, y, 3])
        elif d == 2:
            q.append([x, y, 1])
        elif d == 3:
            q.append([x, y, 0])


for i in range(n):
    for j in range(n):
        if board[i][j] == target:
            target_a, target_b = i+1, j+1 # 타겟 넘버를 찾으면 따로 저장함
        print(board[i][j], end=" ")
    print()
print(target_a, target_b)

'''
이문제는 처음에 출력을 리스트 통쨰로 print(board)를 하는 바람에 틀렸지만
알고보니 하나씩 출력하는 것이었다(나의 착각)
'''