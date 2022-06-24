n = int(input())
# 병사 수
r = list(map(int, input().split()))
# 병사의 전투력
r.reverse()
# 내림차순으로 되어있기때문에 LIS를 쓰기위해 돌려줌

dp = [1] * n

for i in range(n):
    for j in range(0, i):
        if r[i] > r[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        # 맨처음 값부터 i까지 비교후 앞의 값보다 현재 값이 더 클 경우 max 값을 더함

print(n - max(dp))
# 숫자가 꾸준히 늘경우 무조건 수가 증가만 했기때문에 전체수에 max를 빼면
# 증가하지 못한 수의 개수를 구할수가 있다.