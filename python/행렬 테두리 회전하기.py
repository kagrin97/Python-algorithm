def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns + 1)] for j in range(rows + 1)]  # 0,0,0,보드판생성(계산용이하게 1씩더)
    num = 1
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            matrix[row][column] = num  # (1,1)부터 (r+1,c+1)까지 1 ~ r*c까지 추가
            num += 1

    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]  # 하나 빼놓는다
        mini = tmp  # 최초 최소값을 설정

        for k in range(x1, x2):  # 좌측
            test = matrix[k + 1][y1]  # 옮길 숫자
            matrix[k][y1] = test  # 바뀐 숫자
            mini = min(mini, test)  # 최소값을 찾는다

        for k in range(y1, y2):  # 하단
            test = matrix[x2][k + 1]
            matrix[x2][k] = test
            mini = min(mini, test)

        for k in range(x2, x1, -1):  # 우측
            test = matrix[k - 1][y2]
            matrix[k][y2] = test
            mini = min(mini, test)

        for k in range(y2, y1, -1):  # 상단
            test = matrix[x1][k - 1]
            matrix[x1][k] = test
            mini = min(mini, test)

        matrix[x1][y1 + 1] = tmp  # 남은 숫자 push
        answer.append(mini)  # 작은값을 넣어줌

    return answer
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))