import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

def bf(start):
    dist[start] = 0
    for i in range(n): # n번의 라운드 반복
        for j in range(m): # 모든 간선 확인
            cur = edges[j][0] # 출발노드
            next_node = edges[j][1] # 도착노드
            cost = edges[j][2] # 비용
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost: 
                # 현재 거처가는 방법이더 짧은경우
                dist[next_node] = dist[cur] + cost
                if i == n-1: # n번째 라운드에서 값이 갱신된다면 음수 순환이 존재
                    return True
    return False

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

minus_cycle = bf(1)

if minus_cycle:
    print('minus_cycle')
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("no way")
        else:
            print(dist[i])

'''
벨만포드 알고리즘은 간선의 값이 음수이고 음수순환이 존재한다면
써야하는 알고리즘 방식이다 일반적인 다익스트라 방식보다는 
느리지만 음수 값이 존재한다면 써야할 알고리즘이다
'''