N = int(input())
p = [0] + list(map(int,input().split())) # 자리수 맞추기
dp = [0 for _ in range(N+1)] 

for i in range(1,N+1):
    for k in range(1,i+1): # 해당카드를 첨부터 헤당카드까지 비교
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])

'''
dp[n] = n을 만드는 방법은 n번 카드 1개, 혹은 1과 dp[n-1],
혹은 p[2]와 dp[n-2], ..p[i]와 dp[n-i]를 만드는 것 중 중 큰 수
이기 때문에 점화식은 
dp[i] = dp[i-k] + p[k]
'''