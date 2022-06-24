INF = int(1e9)

n, m = map(int, input().split()) # n=노드, m=경로
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0 # 자기 자신노드는 0으로

for _ in range(m):
    a, b = map(int, input().split()) # a=출발노드, b=도착노드
    graph[a][b] = 1 # 모든 도로는 거리가 1이다
    graph[b][a] = 1

x, k = map(int, input().split()) # x=최종노드, k=거쳐가는 노드

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(a, n+1):
            graph[a][b] = graph[b][a] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x] # 총 비용 계산

if result >= INF:
    print(-1)
else:
    print(result)

'''
이 문제는 노드의 수가 100개로 충분히 플로이드 워셜을 사용해도 된다
'''


