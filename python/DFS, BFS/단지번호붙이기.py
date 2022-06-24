n = int(input())
apart = [list(map(int, input())) for _ in range(n)]
# 띄어쓰기를 하지않은 수열들을 n만큼 입력 받는다
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

count = 0 # 단지내 아파트 수
apart_cnt = [] # 총 단지내 아파트수


check = [[False] * n for _ in range(n)]

def dfs(x, y):    
    global count
    count += 1
    check[x][y] = True  # 다시 돌지 못하도록 true
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if apart[nx][ny] == 1 and check[nx][ny] == False:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if apart[i][j] == 1 and check[i][j] == False:
            count = 0 # 아파트수 초기화
            dfs(i, j)
            apart_cnt.append(count)

print(len(apart_cnt)) # 총 단지 수
apart_cnt.sort()
for i in apart_cnt: # 총 단지내 아파트 수 나열
    print(i)

'''
위 문제는 sys.stdin.readline을 사용하면 2번라인에서
에러가 발생해서 이유를 몰라 애를 엄청 먹었던 문제이다
'''