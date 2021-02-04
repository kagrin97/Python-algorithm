import sys

n = int(sys.stdin.readline())

dp = [[0 for i in range(10)]for j in  range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
    
print(sum(dp[n]) % 1000000000)

'''
처음에 문제 이해를 잘못해서 시간이 오래 걸렸다
최대 크기의 2차원 배열을 생성한 뒤에 초기 값을 1씩 넣어 생성해준다
만약 0이라면 1에 자리수 하나만 더해주고 9라면 8하나만 올수 있어서 더해준다
그리고 1~8 이라면 양쪽 대각선 값을 더해준다 
이해를 위한 주소 -> https://pacific-ocean.tistory.com/151
'''