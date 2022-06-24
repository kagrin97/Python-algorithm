import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    board[x][y] = 1 # 1 == 통과했다
    move = [d] # 이동방향
    for _ in range(g): 
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i-1] + 1) % 4) # 다음세대 이동방향 
        move.extend(tmp)
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        board[nx][ny] = 1
        x, y = nx, ny

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            result += 1
                
print(result)

'''
이 문제는 규칙성이 있따
2세대 : 0 1 2 1
3세대 : 0 1 2 1 2 3 2 1
2세대를 거꾸로 뒤집고 +1씩 더해주면 3세대가 된다 (15줄)
'''