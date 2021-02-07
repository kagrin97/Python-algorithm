import sys
input = sys.stdin.readline

n, k = map(int, input().split())
backpack = []
for _ in range(n):
    backpack.append(list(map(int, input().split())))


dp = [0] * n
if backpack[0][0] <= k:
    dp[0] = backpack[0][0]
else:
    dp[0] = 0
result = [0] * n
result[0] = backpack[0][1]

for i in range(1, n):
    if dp[i-1] <= k :
        if dp[i-1] + backpack[i][0] <= k:
            dp[i] = dp[i-1] + backpack[i][0]
            result[i] = result[i-1] + backpack[i][1]
        else:
            dp[i] = backpack[i][0]
            result[i] = backpack[i][1]


print(result[dp.index(max(dp))])

