def solution(n):
    answer = 0

    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]


n = 4
print(solution(n))

'''
피보나치여라~
'''