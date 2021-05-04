def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]
    
    # 1 ~ row*col까지 숫자가 들어간 보드 만들기
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            board[i-1].append((i-1)*columns+j)

    for x1, y1, x2, y2 in queries:
        temp = board[x1-1][y2-1] # 오른쪽위 대각선값 저장
        min_value = 10001
        
        # 북쪽 테두리
        min_value = min(min(board[x1-1][y1-1:y2-1]), min_value)
        board[x1-1][y1:y2] = board[x1-1][y1-1:y2-1]

        # 서쪽 테두리
        for i in range(x1, x2):
            min_value = min(board[i][y1-1], min_value)
            board[i-1][y1-1] = board[i][y1-1]
        
        # 남쪽 테두리
        min_value = min(min(board[x2-1][y1:y2]), min_value)
        board[x2-1][y1-1:y2-1] = board[x2-1][y1:y2]

        # 동쪽 테두리
        for i in range(x2-2, x1-2, -1):
            min_value = min(board[i][y2-1], min_value)
            board[i+1][y2-1] = board[i][y2-1]
        
        board[x1][y2-1] = temp 
        min_value = min(min_value, temp)
        # 북쪽 테두리 변화로 변화된값에 의해 오른쪽위 대각선 바로 아래 값이
        # 이상하게 변하기 때문에 따로 저장해서 넣어줌
        
        answer.append(min_value)
    
    return answer
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))