from copy import deepcopy
import sys
input = sys.stdin.readline
def watch(x, y, office, d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if office[nx][ny] == 6: # 벽을 만나면 종료
                    break
                elif office[nx][ny] == 0: # 0을만나면 #으로 바꿈
                    office[nx][ny] = "#"
            else: # 범위를 벗어나면 종료
                break
def dfs(office, cnt):
    global result
    tmp = deepcopy(office) 
    if cnt == cctv_cnt: # 모든 cctv를 검사했으면
        num = 0
        for i in range(n):
            num += tmp[i].count(0)
        result = min(result, num) # 사각지대 최소값을 넣어줌
        return
    x, y, cctv = cctv_info[cnt] # 해당 cctv정보를 빼냄
    for i in direction[cctv]: # 해당 cctv의 모든 경우의 방향을 가져옴
        watch(x, y, tmp, i) 
        dfs(tmp, cnt + 1) # 재귀 함수로 모든 cctv를 검사함
        tmp = deepcopy(office) 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]], 
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
# 1~5번까지 방법으로 바라보는 방향은 4,2,4,4,1 가지의 방법이있고 그에따른 방향이다
n, m = map(int, input().split())
office = []
cctv_info = []
cctv_cnt = 0
result = 100000000 # 최대값 갱신을위한 

for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(len(office[i])):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv_info.append([i, j, office[i][j]]) # cctv를 발견하면 좌표와 cctv종류를 넣는다
            cctv_cnt += 1 

dfs(office, 0)
print(result)