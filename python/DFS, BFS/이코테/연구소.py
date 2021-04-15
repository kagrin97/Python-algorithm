import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)] # 초기 입력받을 값 배열
temp = [[0] * m for _ in range(n)] # 3벽 설치뒤 맵 리스트

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#    상  우  하  좌
result = 0

def virus(x, y): # bfs
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m: # 벽을 세울수 있으면
            if temp[nx][ny] == 0: # 벽을 퍼트릴수 있는 공간을 만나면
                temp[nx][ny] = 2
                virus(nx, ny) # 재귀적으로 반복


def get_score():
    score = 0 # 초기화
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: # 모두 검사해서 0을 만나면 count 증가
                score += 1
    return score 

def dfs(count):
    global result
    if count == 3: # 벽이 3개가 세워졌으면
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j] # 3개벽과 나머지 벽들 모두를 temp에 세워주기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2: # 바이러스를 만나면 바이러스 퍼트리기
                    virus(i, j)
        result = max(result, get_score()) # 바이러스 퍼트리고 나서 0개수 구하기
        return   
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0: # 벽을세울수 있으면
                data[i][j] = 1 # 벽을세우고
                count += 1 
                dfs(count)  # 3개가 세워질때까지 실행
                data[i][j] = 0 #벽 초기화 (3개를 세운후 0값을 계산후)
                count -= 1 

dfs(0)
print(result)

'''
본문제는 벽을 3개를 설치하고 바이러스를 퍼트리고 남은 0의 개수를 구하고
이것을 계속 반복한 후에 0의개수가 가장많은 값을 출력한다
'''