INF = int(1e9)
n, m = map(int, input().split()) # n=노드개수, m=간선개수
start = int(input()) # 시작노드
graph = [[] for i in range(n+1)] # 각 노드에 연결되있는 노드 정보
visited = [False] * (n+1) # 방문한적이 있는지
distance = [INF] * (n+1) # 최소 노드의 비용

for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c)) # a=노드, b=도착노드, c=비용

def get_smallest_node(): # 방문하지 않은 노드중 가장짧은 노드 반환
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] #해당 노드에 비용을 넣어줌
        for i in range(n-1): # 시작노드를 제외한 전체 반복
            now = get_smallest_node()
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] + j[1] # 현재노드를 거쳐서 이동하는 비용이 더적을경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('no')
    else:
        print(distance[i])




