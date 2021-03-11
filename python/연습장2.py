import re

def solution(m, n, board):
    count = 0
    s = 0
    while s < 5:
        s+=1
        ss = set()
        new = []
        for i in range(m):
            stack = []
            for j in range(n):
                try:
                    stack.append(board[i][j])
                except:
                    pass
            new.append(stack)

        board = new
        print(board)

        for i in range(n):
            for j in range(m):
                try:
                    if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                         for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
                             ss.add((x,y))
                except:
                    pass
        
        count += len(ss)
        ss = sorted(ss)
        for x, y in ss:
            board[x][y] = '_'
        
        for i in range(len(board)):
            while '_' in board[i]:
                board[i].remove('_')

    return count
    
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))