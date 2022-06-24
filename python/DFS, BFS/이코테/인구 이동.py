from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
# 땅의 크기 n, l <= 연합이 될수있는 인원 <= r
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    # 전체 나라의 정보
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

total_count = 0

def process(x, y, index):
    united = [] # x, y 와 연결된 나라 index를 담음
    united.append((x, y))
    q = deque() 
    q.append((x, y))
    union[x][y] = index # 연합의 번호 할당
    summary = graph[x][y] # 연합의 총 인구를 구하기 우한 변수
    count = 1 # 연합의 수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1: # 상하좌우중 검사를 안한 나라 일 경우
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r: # 그중 두 나라 인구수를 뺀값이 l <= c <= r
                    q.append((nx, ny)) # 다음 검사할 나라를 다음 나라로 바꿔줌
                    union[nx][ny] = index # 다음 나라도 연합 번호 할당
                    summary += graph[nx][ny] # 총 인구수
                    count += 1 # 연합안의  나라 개수
                    united.append((nx, ny)) # 모든 연합의 평균을 구하기 위한 스택
    for i, j in united: #  연합의 각각의 인덱스 
        graph[i][j] = summary // count # 평균을 구해서 넣어줌
    return count # while문이 끝나면 연합안의 나라 개수를 리턴

while True:
    union = [[-1] * n for _ in range(n)] # 검사할 목록 생성
    index = 0  
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 만약 검사안한 나라를 발견하면 
                process(i, j, index) # 함수 실행 
                index += 1 # 모든 검사를 체크하는 변수
    if index == n * n: # 모든 검사를 했을 경우 탈출
        break
    total_count += 1 # 연합하나를 검사 할때마다 갯수 증가

print(total_count) # 총 연합이 만들어진 수(국경 개방)

