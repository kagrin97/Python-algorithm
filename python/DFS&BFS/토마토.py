import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])
            # 익은 토마토만 q에 넣어준다

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
time = -1 

while q:
    time += 1 # q가 한번만 실행되면 time은 0이된다(한번만실행 된다는 것은 모든 값이 1이라는 뜻) 
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = 1 

check = True

for i in graph:
    if 0 in i:
        check = False
        print(-1)
        break
        # 익지 않은 토마토가 있으면 -1출력
if check:
    print(time)
    # 실행된 횟수로 총 익는데 걸린 시간을 알수있다.

'''
위 문제는 time 변수를 쓰는것이 관건이다
'''
        