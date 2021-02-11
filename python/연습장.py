import sys
input = sys.stdin.readline

n = int(input())
apart = []
for _ in range(n):
    apart.append(list(map(int, input())))

count = 0
apart_cnt = []

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def dfs(x, y):
    global count
    apart[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and apart[nx][ny] == 1:
            dfs(nx, nx)
    


for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            count = 0
            dfs(i, j)
            apart_cnt.append(count)


print(len(apart_cnt))
apart_cnt.sort()

for i in apart_cnt:
    print(i)