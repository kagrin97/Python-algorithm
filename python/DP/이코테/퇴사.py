n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)

'''
최대 값을 알기위해 현재 가능한 상담시간이 최대 상담 개수를 초과 하지
않는다는 if 문부터 시작한다 뒤에서 부터 시작하는 이유는 그래야 딱 맞게
상담이 끝나기 때문이다.
현재i의 price와 상담시간을 합치고 그 값을 저장한다음에 
최대 값과 계속 비교를 한다 
'''