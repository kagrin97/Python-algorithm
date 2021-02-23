def solution(n):
    graph = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0 # x값을 0으로 시작하기 위함
    num = 1

    for i in range(n):
        for j in range(i, n):
            # 위 for문을 쓸 경우 점점 최대 반복 횟수가 줄어들게 됨
            if i % 3 == 0:
                x += 1
                # down
            elif i % 3 == 1:
                y += 1
                #right
            elif i % 3 == 2:
                x -= 1
                y -= 1

            graph[x][y] = num
            num += 1
    
    for i in graph:
        for j in i:
            if j != 0:
                answer.append(j)
           
    return answer

n = 5
print(solution(n))



