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
                # right
            elif i % 3 == 2:
                x -= 1
                y -= 1
                # left_up 
            graph[x][y] = num
            num += 1
            # 실질적인 값 넣기
    for i in graph:
        for j in i:
            if j != 0:
                answer.append(j)
           # 첫줄부터 확인 하면서 0이아니면 리스트 삽입
    return answer

n = 5
print(solution(n))

'''
if i % 3 == 0 때문에 착각하기 쉬운데 if i % 3 == 0을 쓰는 이유는
단순히 3번을 반복하기 위해서이다 아래,오른,왼위(크게 의미가 없다)
반복문을 돌 때마다 i값이 늘면서 2번째 for문은 1씩 덜 반복한다
'''



