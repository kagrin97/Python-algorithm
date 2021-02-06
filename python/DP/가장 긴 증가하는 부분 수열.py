a = int(input())

arrary = list(map(int, input().split()))

dp = [1] * a

for i in range(a):
    for j in range(i):
        if arrary[j] < arrary[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(max(dp))

'''
위 문제는 i,j개 먼지 헷갈렸는데 i가0일경우 j 부분은 아예
실행되지 않으면 i가2일 경우 a는 2번 실행이된다
'''
