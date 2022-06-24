n = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[n])

'''
피보 나치 수열과 같은 점화식을 쓴다
(계산 해보면 피보나치 수열임)
'''