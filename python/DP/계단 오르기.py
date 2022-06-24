import sys
input = sys.stdin.readline
n = int(input())

dp = []
array = []

for i in range(n):
    array.append((int(input())))


dp.append(array[0])
# 첫번쨰 계단 할당
if len(array) >= 2:
    dp.append(max(array[0] + array[1], array[1]))
# 두번째 계단 2번 밟거나 1번 밟거나
if len(array) >= 3:
    dp.append(max(array[0] + array[2], array[1] + array[2]))

for i in range(3, n):
    if len(array) >= 3:
        dp.append(max(dp[i-2] + array[i] , dp[i-3] + array[i] + array[i - 1]))
        # 두가지 경우중 가장 큰 경우 할당
    else:
        pass


print(dp.pop())

'''
위 문제는 계단의 길이가 2개나 1개 밖에 없을 경우에는 에러가 나기때문에
if문을 썻다
''' 