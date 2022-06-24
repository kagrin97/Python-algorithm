n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

k = 2

for i in range(1, n):
    for j in range(k):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        elif i == j:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]
    k += 1
print(max(dp[n - 1]))

'''
이코테 코드로 백준에 제출 했을시 오류가 나온다
이코테의 경우 맨왼쪽과 맨오른쪽만 가진 2번째 열에서는 중간 값이 업어
값을 0을 더하게 되어서 오류가 뜬것으로 보인다
그리고 k의 경우 이코테는 range(0,i)로 만약 i가 1일 경우 2번실행이 아닌 딱 
한번만 실행이 되기 때문에 마찬가지로 2번째 열에서 오류가 발생한다
(하지만 예제1은 통과가 된다 이해가 잘 안간다😢)
'''
