import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
act = list(map(int, input().split()))

for a in act:
    if a == 1:              # 상하 반전
        tmp = [[0] * m for _ in range(n)]
        for i in range(n):
            tmp[i] = board[n-1-i]
        board = tmp

    elif a == 2:            # 좌우 반전
        tmp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                tmp[i][j] = board[i][m-1-j]
        board = tmp

    elif a == 3:            # 오른쪽으로 90도
        tmp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp[i][j] = board[n-1-j][i]     # 행,열 길이가 다르기 때문에 행열을 바꿔 갱신
        board = tmp
        n, m = m, n         # 행,열 길이가 다르기 때문에 90도 돌릴때마다 행,열을 바꿔준다

    elif a == 4:            # 왼쪽으로 90도
        tmp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp[i][j] = board[j][m-1-i]
        board = tmp
        n, m = m, n

    elif a == 5:
        tmp = [[0] * m for _ in range(n)]
        for i in range(n // 2):  # move position: 1 -> 2
            for j in range(m // 2):
                tmp[i][j + m // 2] = board[i][j]

        for i in range(n // 2):  # move position: 2 -> 3
            for j in range(m // 2, m):
                tmp[i + n // 2][j] = board[i][j]

        for i in range(n // 2, n):  # move position: 3 -> 4
            for j in range(m // 2, m):
                tmp[i][j - m // 2] = board[i][j]

        for i in range(n // 2, n):  # move position: 4 -> 1
            for j in range(m // 2):
                tmp[i - n // 2][j] = board[i][j]

        board = tmp

    elif a == 6:
        tmp = [[0] * m for _ in range(n)]
        for i in range(n // 2):         # 1 -> 4
            for j in range(m // 2):
                tmp[i + n // 2][j] = board[i][j]

        for i in range(n // 2, n):      # 4 -> 3
            for j in range(m // 2):
                tmp[i][j + m // 2] = board[i][j]

        for i in range(n // 2, n):      # 3 -> 2
            for j in range(m // 2, m):
                tmp[i - n // 2][j] = board[i][j]

        for i in range(n // 2):      # 2 -> 1
            for j in range(m // 2, m):
                tmp[i][j - m // 2] = board[i][j]

        board = tmp

for i in board:
    print(*i)
