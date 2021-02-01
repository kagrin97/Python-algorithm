n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, i):
        if i == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        if i == j:
            up = 0
        else:
            up = dp[i - 1][j]
        
        dp[i][j] = dp[i][j] + max(up, up_left)

print(max(dp[n - 1]))

''' 
위 경우는 2가지 가 존재하는데 왼쪽 위에서 내려오는 경우와 바로 위에서 내려오는 경우
가 존재한다 (배열의 특성을 잊지말자) 전체적으로 금광과 비슷한 문제이다
'''