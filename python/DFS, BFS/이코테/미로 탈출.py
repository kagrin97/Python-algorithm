from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 초기값 삽입
    while queue: # 큐가 빌때 까지 반복
        x, y = queue.popleft()
        for i in range(4): # 현재위치에서 4번 반복
            nx = x + dx[i] # 현재위치에서 x 만큼이동
            ny = y + dy[i] # 현재위치에서 y 만큼이동
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            # 범위를 벗어 날 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 괴물이 있을 경우 무시
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            # 도망갈 곳이 있다면 현재 위치에 전 위치의 이동 카운트에서 +1
            # 그리고 전에 위치가 빠졌으므로 현재위치를 삽입

    return graph[n - 1][m - 1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#    상  하  좌  우
print(bfs(0, 0))

'''
미로 탈출 문제
bfs 문제로 상하좌우 확인후에 1인 값을 발견하면 그곳으로 이동후
count 값을 1올려서 최단 거리를 구할수가 있다 
삽입과 추출이 계속 이어져야 한다 
'''