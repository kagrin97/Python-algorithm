def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
        # 주어진 범위를 벗어나면 종료
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 현재 노드가 방문하지 않은거라면 방문처리를 한다
        dfs(x - 1, y) # 상
        dfs(x, y - 1) # 좌
        dfs(x + 1, y) # 하
        dfs(x, y + 1) # 우
        return True # 모두 채웠으면 true 리턴
    return False # 현재 노드가 0이 아니라 1 이면 false 리턴


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            # 재귀함수로 0들 묶음을 1로 다 채웠다면 result 1 추가

print(result)

'''
음료수 얼려 먹기
'''