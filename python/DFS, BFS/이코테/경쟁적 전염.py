from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# n = nxn실험관  ,  k = 바이러스 종류
graph = [] # 전체보드
data = [] # 바이러스에 대한 정보를 담는

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
            # 바이러스를 집어 넣었을 경우 ((바이러스종류, 시간, x, y))를 삽입

data.sort() # 정렬이후 큐로 옮기기 (낮은번호부터 증식하므로)
q = deque(data)

target_s, target_x, target_y = map(int, input().split())
# 끝나는 시간 x , y 입력
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft() # 종류, 시간, x, y를 꺼냄 
    if s == target_s: # 원하는 s일경우 종료
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n: 
            if graph[nx][ny] == 0: # 증식 가능할경우
                graph[nx][ny] = virus # 증식
                q.append((virus, s + 1, nx, ny)) # 다음 검사할 값을 넣어줌

print(graph[target_x - 1][target_y - 1])

'''
이문제는 bfs로 풀수가 있으며 우선순위가 낮은 번호부터 있기 때문에 오름차순 정렬을
해준다 그리고나서 모든 곳을 검사를 한다음에 원하는 시간과 위치를 출력한다
'''