n = int(input())
boom = [list(str(input())) for _ in range(n)]   # 폭탄 위치 리스트
check = [["."] * n for _ in range(n)]           # 내가 밟은 리스트

dx = [-1,-1,-1, 0,0, 1,1,1]                     # 8방향
dy = [-1,0,1, -1,1, -1,0,1]

big_boom = False                    # 폭탄을 밟았는지 여부

for i in range(n):
    string = list(str(input()))
    for j in range(n):
        if string[j] == 'x':        # 내가 밟았으면
            if boom[i][j] == '*':   # 밟았는데 폭탄이였으면
                big_boom = True
                continue
            boom_cnt = 0            # 주위 폭탄 갯수
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if boom[nx][ny] == '*':     # 8방향을 다검사해서 폭탄있으면 cnt추가
                        boom_cnt += 1
            check[i][j] = str(boom_cnt)

if big_boom:                  # 만약 폭탄을 밟았으면 폭탄위치와 주위 폭탄갯수를 보여줌
    for i in range(len(boom)):
        for j in range(len(boom[i])):
            if boom[i][j] == '*':
                check[i][j] = "*"

for i in check:             # 폭탄을 안 밟았으면 주위 폭탄갯수만 보여줌
    print("".join(i))

# 이 문제는 폭탄을 밟았다는 가정에 대한 예제라든가 설명이 부실해서 어려웠던문제이다
# 설명만 제대로 했으면 쉬운문제인데 아오