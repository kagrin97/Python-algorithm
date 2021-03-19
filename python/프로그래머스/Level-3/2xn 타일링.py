def solution(n):
    answer = 0

    dp = [0] * 60001

    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        
    return dp[n] % 1000000007

n = 4
print(solution(n))

'''
n이 1일떄와 2일때를 자세히 보니까 피보나치 수열이었다
% 1000000007를 마지막 return 할때 사용하면 시간초과가 발생한다
'''