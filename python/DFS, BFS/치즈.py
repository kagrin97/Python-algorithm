from collections import deque

def bfs():
    q = deque()
    q.append([0, 0]) # 0,0은 치즈가 없기때문에 시작위치로 지정
    check = [[-1] * m for _ in range(n)] # 방문했는지
    check[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == -1: # 방문하지 않았다면
                    if board[nx][ny] >= 1: # 치즈라면 +1
                        board[nx][ny] += 1
                    else: 
                        check[nx][ny] = 0 # 치즈가 아닐경우 방문처리후 현재좌표 갱신
                        q.append([nx, ny])

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
time = 0
cnt = [] # 남아있는 치즈의 수

while True:
    bfs()
    flag = 0
    cheese_cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2: # 치즈 겉에부분이라면 0으로
                board[i][j] = 0
                cheese_cnt += 1 
                flag = 1
    if flag: # 남아있는 치즈가 있었다면 시간추가밑 치즈수+
        time += 1
        cnt.append(cheese_cnt)
    else:
        break
print(time)
print(cnt[-1])

'''
이 문제를 쉽게 풀려면 15~ 20줄이 중요한데
0과 맞닿은 1은 +1해줘서 겉에를 표시해주고 다음 좌표에 1이 있었던곳을 가지 않으므로
내부에있는 치즈는 +1을 하지 않게 작용한다
'''