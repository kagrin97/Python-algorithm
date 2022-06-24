import sys
input = sys.stdin.readline

n, k = map(int, input().split())
table = [ [0]*(k+1) for _ in range(n+1) ]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j < w:
            table[i][j] = table[i-1][j]
            # 현재 가능한 무게가 초과 되었을시 전값을 그대로 가져옴
        else:
            table[i][j] = max(table[i-1][j], table[i-1][j-w] + v)
            # 무게를 수용할수 있을경우 가져가거나, 안가져가는 것중 이득을 넣음
            
print(table[n][k])


'''
이문제는 dp문제중 냅색문제이다 0-1배낭문제로 나눠지지 않을때 쓴다(그리드x)
2차원 배열을 만들고 j는 현재 넣을수 있는 무게, i는 무게와 가치를 포함한다
1. 가져가지 못할 무게일 경우 가져가지 않는다 (10번줄)
2. 수용가능 무게일 경우 안가져가는 경우와, 가져가서 다음 물건을 포기
해도 이득일 경우 중 최대 가치를 값을 가져간다
table[i][j] = max(table[i-1][j], table[i-1][j-w] + v)
table[i-1][j-w] + v = table[아이템 i-1][무게 j- 현재아이템 i 무게] + 현재아이템 가치 i
'''

