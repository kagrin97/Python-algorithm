n = int(input())
board = [0] * n

a = 1
for i in range(n):
    board[i] = a
    a += 1

while len(board) >= 2:
    tmp = []
    for i in range(len(board)):
        if i % 2 != 0:
            tmp.append(board[i])
    board = tmp

print(*board)