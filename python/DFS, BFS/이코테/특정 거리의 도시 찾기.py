from collections  import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
# 도시개수, 도로개수, 필요한 거리, 시작위치
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # [[], [2, 3], [3, 4], [], []]  = 1번인덱스(1번도시)와 연결된 도로는 2,3번이다
distance = [-1] * (n + 1)
distance[x] = 0
# x와의 k만큼 떨어진 수를 찾기위한 리스트
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]: # 1번인덱스의 도로부터 끝까지
        if distance[next_node] == -1: # 방문하지 않았다면
            distance[next_node] = distance[now] + 1 # 최단거리 갱신
            q.append(next_node) # 출발위치 갱신

check = False 
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
    # 하나씩 조사해서 k만큼 떨어진 도로를 출력(오름차순)
if check == False:
    print(-1)
    # 하나도 없다면 -1 출력

'''
특정 거리의 도시 찾기
모든 도로의 거리는 1이라는 조건덕분에 bfs를 이용한 최단거리를 찾을 수 있다
x를 시작점으로 bfs를 수행하여 모든 도시의 최단거리를 계산 한다음에
각 최단거리를 하나씩 확인해서 k 라면 해당 도시의 번호를 출력한다
'''