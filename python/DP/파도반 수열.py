t = int(input())

def triangle(n):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 3])
    return dp

for _ in range(t):
    dp = [0] * 101
    n = int(input())
    dp.append(triangle(n))
    print(dp[n])

'''
위 문제는 문제를 자세히 보니 점화식을 알아 차릴수 있었다
dp[i] = (dp[i - 2] + dp[i - 3])
'''