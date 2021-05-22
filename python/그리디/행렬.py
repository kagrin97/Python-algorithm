N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

def change(x, y, A):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j] 
            # 실제로 뒤집어 버림

cnt = 0
for i in range(0, N-2): # 3X3단위로 뒤집기때문에 맨뒤에서3번쨰 까지 실행함
    for j in range(0, M-2):
        if A[i][j] != B[i][j]: # 다르면 뒤집는다
            cnt += 1
            change(i, j, A)

if A != B: # 다뒤집고나서도 값이다르면 -1 출력및 종료
    print(-1)
    exit()
print(cnt)

'''
이문제는 2차원 배열 A -> B로 치환이 가능한가를 물어보는 문제이다
항상 3X3 단위로 모든 수를 뒤집어야 한다
'''

