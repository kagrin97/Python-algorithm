from itertools import combinations # 모든 수열의 조합을 알려줌
import sys
input = sys.stdin.readline

n = int(input())
board = [] # 기본 위치 정보
teachers = [] # 선생님 위치 정보
spaces = [] # 빈공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j)) # 선생을 만나면 위치정보를 넣음
        if board[i][j] == "X":
            spaces.append((i, j)) # 빈 공간을 만나면 넣음


def watch(x, y, direction):
    if direction == 0: # 왼쪽부터 조사
        while y >= 0: # 왼쪽벽에 닿을 때까지
            if board[x][y] == "S": # 학생을 만나면 TRUE 반환
                return True 
            if board[i][j] == "O": # 장애물을 만나면 FALSE 반환
                return False
            y -= 1 # 왼쪽 모든 값을 구하기 위해 뺴주기
    if direction == 1: # 오른쪽
        while y < n:
            if board[x][y] == "S":
                return True
            if board[i][j] == "O":
                return False
            y += 1
    if direction == 2: # 위쪽
        while x >= 0:
            if board[x][y] == "S":
                return True
            if board[i][j] == "O":
                return False
            x -= 1
    if direction == 3: # 아래쪽
        while x < n:
            if board[x][y] == "S":
                return True
            if board[i][j] == "O":
                return False
            x += 1
    return False # 4방향 모두에서 찾을수 없으므로 FALSE 반환
        
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i): # 선생님 위치정보와 4방향을 매개변수로 주어짐
                return True # 찾았을 경우 TRUE 리턴

find = False

for data in combinations(spaces, 3): # 빈공간중 3개를 뽑는 모든 수열
    for x, y in data:
        board[x][y] = "O" # 장애물 설치
    if not process(): # 학생을 찾지 못 했을경우
        find = True 
        break
    for x, y in data: # 학생을 찾았을 경우 장애물 치우기
        board[x][y] = "X"
    
if find: # 학생을 발견 못했을 경우
    print('YES')
else:
    print('NO')

