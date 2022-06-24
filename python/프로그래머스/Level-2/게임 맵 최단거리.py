from collections import deque

def solution(maps):

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((0,0)) # 초기값

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                

    if maps[-1][-1] != 1: # 도착했으면 도착 지점 거리값을 출력
        return maps[-1][-1]
    else: 
        return -1 # 도착을 못했음 -1
    
m = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(m))

'''
이코테 미로 탈출과 매우 흡사한 문제이다
'''