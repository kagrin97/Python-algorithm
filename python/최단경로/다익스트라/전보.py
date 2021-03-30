import heapq

INF = int(1e9)
n, m, start = map(int, input().split()) # n=노드개수, m=간선개수, start=시작노드
graph = [[] for i in range(n+1)] # 각 노드에 연결되있는 노드 정보
distance = [INF] * (n+1) # 노드의 비용

for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c)) # a=노드, b=도착노드, c=비용

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 힙을사용해 더빠름
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 지금 비교할려는 값이 전값보다 크면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1] # dist현재비용, i[1] 다음 간선비용
            if cost < distance[i[0]]: # i[0] 다음 간선노드 인덱스
                distance[i[0]] = cost # 적은비용 갱신
                heapq.heappush(q, (cost, i[0])) # 다음정보 추가

dijkstra(start)

count = 0 # 전보가 도착한 도시의 수
max_value = 0 # 가장 오래걸린 도시의 시간
for d in distance:
    if d != INF:
        count += 1
        max_value = max(max_value, d)
print(count-1, max_value) # 시작한노드는 빼줘야 함 count-1