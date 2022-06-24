import copy
t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    if 0 < d:           # 오른쪽으로
        spin_cnt = d // 45
        for _ in range(spin_cnt):
            a = n // 2
            board_copy = copy.deepcopy(board)
            col = []
            for i in range(n):          # 중앙 세로 -> 오른 대각
                col.append(board[i][a])
            for i in range(n):
                board_copy[n-1-i][i] = col.pop()

            r_diagonal = []             # 오른 대각 -> 중앙 가로
            for i in range(n):
                r_diagonal.append(board[n-1-i][i])
            for i in range(n):
                board_copy[a][i] = r_diagonal.pop(0)

            mid_line = []               # 중앙 가로 -> 왼쪽 대각
            for i in range(n):
                mid_line.append(board[a][i])
            for i in range(n):
                board_copy[i][i] = mid_line.pop(0)

            l_diagonal = []             # 왼쪽 대각 -> 중앙 세로
            for i in range(n):
                l_diagonal.append(board[i][i])
            for i in range(n):
                board_copy[i][a] = l_diagonal.pop(0)
            board = board_copy

    elif 0 > d:           # 오른쪽으로
        spin_cnt = abs(d // 45)
        for _ in range(spin_cnt):
            a = n // 2
            board_copy = copy.deepcopy(board)

            col = []            # 중앙 세로 -> 왼쪽 대각
            for i in range(n):
                col.append(board[i][a])
            for i in range(n):
                board_copy[i][i] = col.pop(0)

            l_diagonal = []     # 왼쪽 대각 -> 중앙 가로
            for i in range(n):
                l_diagonal.append(board[i][i])
            for i in range(n):
                board_copy[a][i] = l_diagonal.pop(0)

            mid_line = []           # 중앙 가로 -> 오른 대각
            for i in range(n):
                mid_line.append(board[a][i])
            for i in range(n):
                board_copy[n-1-i][i] = mid_line.pop(0)

            r_diagonal = []
            for i in range(n):
                r_diagonal.append(board[n-1-i][i])
            for i in range(n):
                board_copy[i][a] = r_diagonal.pop()
            board = board_copy
    for i in board:
        print(*i)