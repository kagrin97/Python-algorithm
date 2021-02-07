import sys
input = sys.stdin.readline

n = int(input())
arrary = list(map(int, input().split()))

dp = [0] * n
dp[0] = arrary[0]

for i in range(1, n):
    dp[i] = max(arrary[i], dp[i - 1] + arrary[i])
        
print(max(dp))

'''
위 문제는 값을 입력받고 현재 값과 현재값+이전까지 더해온 값
중에 더큰수로 할당을 받는 방식으로 풀수 있다
max(arrary[i], dp[i - 1] + arrary[i])
max  현재값   ,   이전값    +  현재값
'''