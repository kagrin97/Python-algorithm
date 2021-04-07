import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global count
    if visited[x][y] == 0: # 청소할수 있으면
        visited[x][y] = 2 # 청소완료
        count += 1
    for _ in range(4):
        nd = (d + 3) % 4 # (현재위치+3) % 4 = 왼쪽방향
        nx = x + dx[nd]
        ny = y + dy[nd]
        if visited[nx][ny] == 0: # 왼쪽방향 청소할수 있으면 제귀
            clean(nx, ny, nd)
            return
        d = nd # 현재위치를 다음위치로 바꿔줌
    # 여기 밑에 코드가 실행된다는 것은 4방향다 막히거나 청소됨 
    nd = (d + 2) % 4 # (현재위치+2) % 4 = 뒤쪽방향
    nx = x + dx[nd]
    ny = y + dy[nd]
    if visited[nx][ny] == 1: # 뒤가 벽이면 종료
        return
    clean(nx, ny, d) # 뒤로 이동가능하면 뒤로 이동 (방향은 유지)

n, m = map(int, input().split()) 
x, y, d = map(int, input().split()) # d는 방향 
visited = [list(map(int, input().split())) for _ in range(n)] # 청소구역 

count = 0
clean(x, y, d)
print(count)










    



    




