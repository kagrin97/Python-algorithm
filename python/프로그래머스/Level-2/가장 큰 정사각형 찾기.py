def solution(board):
    row = len(board)
    col = len(board[0])
    answer = []

    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                continue
            # 맨 첫번쨰 값을 실행 시킬 필요는 없다
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                # 현재 값이 0이 아니라면 왼쪽,왼대각석,위 3중 가장 작을값에 1을 더한값을 넣는다
    
    for i in range(row):
        answer.append(max(board[i]))
        # 2차원 배열이므로 값을 꺼내기 위해 한줄에서 가장 큰 값씩 넣어줌
    return max(answer) ** 2
    # 크기가 3인 사각형은 가로 세로가 3이란 소리로 3**2 = 9 즉 값이 9이다

info = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(info))

'''
이문제는 dp로 풀어야하는 문제이다 
https://codedrive.tistory.com/53
이 블로그에서 자세히 설명이 되어 있다
'''

