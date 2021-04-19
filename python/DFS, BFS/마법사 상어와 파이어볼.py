import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split()) # k는 마법사가 명령을 내리는 횟수
board = [[deque() for _ in range(N)] for _ in range(N)]
q = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    board[x-1][y-1].append([m, s, d]) # m=질량, s=속력, d=방향
    q.append([x-1, y-1])

for _ in range(K): 
    temp = []
    qlen = len(q)
    for _ in range(qlen):
        x, y = q.popleft()
        for _ in range(len(board[x][y])): # 해당위치에 있는 파이어볼만큼 실행
            m, s, d = board[x][y].popleft()
            nx = (s * dx[d] + x) % N # n-1과 0번은 이어져있으므로 %N을 해준다
            ny = (s * dy[d] + y) % N
            q.append([nx, ny]) 
            temp.append([nx, ny, m, s, d]) 
    
    for x, y, m, s, d in temp: # 따로 저장해야 중복을 막을수 있다
        board[x][y].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1: # 해당위치에 파이어볼이 여러개 이면
                nm, ns, odd, even, flag = 0, 0, 0, 0, 0
                for idx, [m, s, d] in enumerate(board[i][j]):
                    nm += m # 질량을 합침
                    ns += s # 속력을 합침
                    if idx == 0: # 첫번째 파볼이면
                        if d % 2 == 0: # 짝수면 even+=1
                            even = 1
                        else: 
                            odd = 1 # 홀수면 odd+=1
                    else:
                        if even == 1 and d % 2 == 1:
                            flag = 1
                        elif odd == 1 and d % 2 == 0:
                            flag = 1
                        # 첫 파볼이 짝수인데 다른 파볼이 홀수면 flag를 세움, 반대경우도 마찬가지

                nm //= 5 # 파볼 질량을 나눠줌
                ns //= len(board[i][j]) #파볼 속력도 나눠줌
                board[i][j] = deque() # 현재 파볼 위치 초기화
                if nm != 0: # 질량이 0이 아니라면
                    for idx in range(4):
                        if flag == 0: # 방향이 모두 홀수거나 짝수라면
                            nd = 2 * idx # 0, 2, 4, 6 방향
                        else:
                            nd = 2 * idx + 1 # 1, 3, 5, 7
                        board[i][j].append([nm, ns, nd]) # 후에 이동시킬 파볼을 생성
                    
result = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for m, s, d in board[i][j]:
                result += m
print(result)                    
                    



