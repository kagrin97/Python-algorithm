'''
오큰수
'''

import sys

a = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1 for _ in range(a)]
# -1을 수열 길이만큼 나열및 생성
for i in range(a):
    try:  # 스택에 들은게 없어도 실행되게함
        while n[stack[-1]] < n[i]:
            result[stack.pop()] = n[i]
            # 전값과 현재값중 현재 값이 더클 경우 전값을빼고 현값을 삽입
    except:  # 아무것도 안들어 있을경우 패스
        pass

    stack.append(i)
    # 스택에 아무것도 안들어 있을경우 현재값 삽입
for i in range(a):
    print(result[i], end=" ")
# 하나씩 띄어서 나열
