import sys
sys.setrecursionlimit(10000)
# 재귀 깊이 설정
def dfs(x, y):
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] == 1:
                dfs(nx, ny)
    
t = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)

''' 
위 문제는 9번 줄에 조건식을 if 0 <= nx < n and 0 <= ny < n:
이런식으로 nx < n 으로 줘서 계속 틀리는 바람에 멘탈이 많이 
깨졌던 문제다 
'''
    


