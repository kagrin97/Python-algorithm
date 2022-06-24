import sys
input = sys.stdin.readline


def paper_cut(x,y,n):
    global blue, white
    check = table[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != table[i][j]: # 하나라도 같은색이 아니면 쪼갠다
                paper_cut(x, y, n // 2) # 1사분면
                paper_cut(x, y + n // 2, n // 2) #2 사분면
                paper_cut(x + n // 2, y, n // 2) #3 사분면
                paper_cut(x + n // 2, y + n // 2, n // 2) #4사분면
                return
    
    if check == 0: # 모두 흰색일때
        white += 1
        return
    else: # 모두 파란색일떄
        blue += 1
        return

n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

white = 0 
blue = 0

paper_cut(0,0,n) # 함수 호출
print(white)
print(blue)

'''
 분할 정복 문제로 쿼드 트리 형태이다 조건문이 만족하지 않을시
 4개로 쪼개어 계속 호출해 쪼개 주는 방법이다
 '''




