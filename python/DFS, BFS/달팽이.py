import sys
input = sys.stdin.readline
n = int(input())
num = int(input())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 밑 오른 위 왼쪽
cur_num = n * n                 # 현재값
x, y = 0, 0
direction = 0                   # 초기 방향 
find_num = [1,1]                # 맨처음 숫자를 찾을수도 있으니 꼭 넣어줘야함 

board = [[0] * n for _ in range(n)]     # 실제 값들을 넣을 2차원배열
visited = [[False] * n for _ in range(n)]   # 방문 여부

board[0][0] = cur_num           # 첫번째 값을 넣어줌
visited[0][0] = True            # 방문처리

while 1:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < n and 0 <= ny < n:
        if visited[nx][ny] == False:    # 방문하지 않았으면
            cur_num -= 1
            board[nx][ny] = cur_num
            if cur_num == num:          # 찾는 숫자일 경우 위치를 넣어줌
                find_num = [nx+1,ny+1]
            visited[nx][ny] = True      # 방문처리
            x, y = nx, ny
        else:
            direction += 1      # 이미 방문한 곳이면 방향을 바꿈
            if direction >= 4:
                direction = 0
    else:
        direction += 1          # 배열을 벗어났으면 방향을 바꿈
        if direction >= 4:
            direction = 0

    if cur_num == 1:        # 1까지 실행했으면 종료
        break

for i in board:
    print(*i)

print(*find_num)

# 이 문제는 맨처음 초기값을 찾는 예제를 생각을 못하고 돌려서 런터임 네임에러가 나타났다
# 9 번쨰줄