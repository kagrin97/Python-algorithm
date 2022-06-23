import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = [[0]*n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

for order in range(n**2):
    student = students[order]   # 학생 정보 리스트를 가져옴
    tmp = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:    # 아직 앉지 않았다면
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in student[1:]:    # 좋아하는 학생이라면 좋아요 +1
                            like += 1
                        if board[nx][ny] == 0:          # 비어있다면 공백 +1
                            blank += 1
                tmp.append([like, blank, i, j])

    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))  # like, blank, 행, 열 순으로 정렬
    board[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
students.sort() # 1번부터 n**2명까지 순서대로 점수를 줌

for i in range(n):
    for j in range(n):
        like_cnt = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in students[board[i][j]-1]:# 좋아하는 학생이라면
                    like_cnt += 1
        if like_cnt != 0:
            result += 10 ** (like_cnt-1)
print(result)
