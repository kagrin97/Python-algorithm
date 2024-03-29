from collections import deque
N = int(input()) 
K = int(input()) 
board_array = [[1]*(N+2)] + [[1]+[0]*N+[1] for _ in range(N)] + [[1]*(N+2)]
# 1(벽)으로 둘러싸인 n*n 배열을 만들기위함
for i in range(K):
    a, b = map(int, input().split()) 
    board_array[a][b] = 2 # board의 2는  사과의 위치

L = int(input())
L_array = list(map(lambda x:[int(x[0]), x[1]], [input().split() for _ in range(L)]))
# 뱀의 방향 정보 저장및 정렬

time = 0
x, y = 1, 1
direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} # 0:북 1:동 2:남 3:서
d = 1 
snake_array = deque([[1,1]]) # 뱀의 몸을 표현할 큐
board_array[1][1] = 3 # 뱀의 몸은 3으로 표현

while True:
    x = x + direction[d][0]
    y = y + direction[d][1]
    if board_array[x][y] == 2:
        board_array[x][y] = 3
        snake_array.append([x, y])
        time += 1
    elif board_array[x][y] == 0:
        board_array[x][y] = 3
        snake_array.append([x, y])
        del_x, del_y = snake_array.popleft() # 꼬리 제거
        board_array[del_x][del_y] = 0
        time += 1
    else:
        time += 1
        break
    if len(L_array) != 0:
        if L_array[0][0] == time:
            if L_array[0][1] == 'L':
                d = (d-1) % 4
            else:
                d = (d+1) % 4
            del L_array[0]

print(time)

'''
보통 보편적으로 이런 문제를 풀때는 dx, dy, nx, ny같은 방법을 쓰지만
이 문제를 풀때는 전에 있던 x, y를 저장된 뱀의 꼬리인 snake_array.popleft()를 이용해
구할수가 있었고 북동남서 를 구할때 2개의 배열을 이용하는게 아니라 딕셔너리를 사용해서
해결할수도 있었다
'''

















    



    




