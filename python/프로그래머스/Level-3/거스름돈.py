def solution(n, money):
    
    dp = [1] + [0] * n

    for coin in money:
        for price in range(coin, n+1):
            if price >= coin:
                dp[price] += dp[price - coin]

    return dp[n] % 1000000007
n = 5
money = [1,2,5]	
print(solution(n, money))

'''
dp문제로 동전개수 만큼의 리스트에
차곡차곡 쌓는 방법이다
'''