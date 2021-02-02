n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + dp[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

'''
금광과 매우 유사한 문제지만 금광과 달리 위치 구애 받지않고 선택 할수 있는
가짓수는 무조건 2가지로 만 제한되어서 조금 더 간단하다
전 행에서 2개의 색중 작은 값과 현재 값을 더해 메모제이션 한다
그리고 제일 끝 열에 있는 값중 가장 작은 값을 출력해 준다
'''
