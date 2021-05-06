board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

num = []
for _ in range(5):
    num += list(map(int, input().split()))

check = [0] * 12 #바뀐것의 갯수 저장하는 리스트 idx0~4는 row / 5~9는 col / 10, 11은 대각선
bingo = 0
for n in range(25): #사회자가 하나씩 부른다.
    for i in range(5):
        for j in range(5):
            if num[n] == board[i][j]: # 사회자가 부른숫자 0으로 체크
                board[i][j] = 0
                check[i] += 1 # 해당 행에 체크
                check[j+5] += 1 # 해당 열에 체크
                if i == j: # 대각선
                    check[10] += 1
                if i + j == 4: # 반대 대각선
                    check[11] += 1
                for c in range(12): 
                    if check[c] == 5: # 빙고가 되면
                        check[c] = 0 # 초기회
                        bingo += 1 # 빙고 1+
                        if bingo == 3: # 3빙고면
                            print(n+1) # 순서를 출력하고 종료
                            exit()
