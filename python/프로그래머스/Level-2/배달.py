import math
from collections import deque

def bfs(start, maps, distance, K):
    queque = deque()
    queque.append(start) 
    result = []

    distance[start] = 0 # 처음 값을 넣어줌
    while queque:
        y = queque.popleft()
        for x in range(1, len(maps)):
            if maps[y][x] != 0: # 도착할수있는 곳인 경우
                if distance[x] > distance[y] + maps[y][x] and distance[y] + maps[y][x] <= K:
                    # 현재위치 x > y에서 x 까지의 거리가 더 작을때 x에 더 작은 거리를 넣어줌 
                    distance[x] = distance[y] + maps[y][x]
                    queque.append(x)
    for i in distance:
        if i <= K:
            result.append(i) # k보다 작거나 같은 값만 넣어줌
    return len(result)
            
def solution(N, road, K):
    
    distance = [math.inf for _ in range(N+1)] # math.inf는 항상 최소 값만을 갱신할수 있다
    
    maps = [[0 for _ in range(N+1)] for _ in range(N+1)] # 각각도시의 거리를 2차원 배열화

    for frm, to, w in road:
        if maps[frm][to] == 0 and maps[to][frm] == 0: # 아무런 값이 안들어있으면
            maps[frm][to], maps[to][frm] = w, w # 거리를 넣어줌
        else:
            if w < maps[frm][to]: # 더 짧은 거리를 받으면 갱신을 함
                maps[frm][to], maps[to][frm] = w, w 
    
    return bfs(1, maps, distance, K)

n = 5
r = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
k = 3
print(solution(n, r, k))