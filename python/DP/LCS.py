a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

'''
본 문제는 2차원 배열로 만들어야 풀수있는 문제이다
주의 점이 2차원배열을 1씩 더크게 만들어야 하는데 그이유는 첫번쨰
문자열을 비교할떄 그전의 배열 값을 불러와야 하기 때문에 값이 없더라도
0이라도 존재하야하므로 1씩 더 늘려 주었다
점화식의 아이디어는 a한글자 b전체글자 를 for으로 돌려 전체적으로
검사후에 값이 같으면 1씩 더해주고 아닐경우 옆 숫자를 그대로 가져왔다
'''