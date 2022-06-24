'''
가장 긴 증가하는 부분 수열
'''

from bisect import bisect_left

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
print(dp)

'''
증가하는 수열을 넣을 dp를 생성하고 k는 i를 넣을 인덱스 값을 의미한다
만약 전체 길이보다 k값이 크다는 것은 i가 dp안 수열중 가장 크다는 것을 의미
하기때문에 뒤에 추가해준다.
아닐 경우에는 dp의 k인덱스에 i값을 넣어 준다 즉 i값이 중복 되지 않고 
계속 갱신됨을 의미한다 
'''