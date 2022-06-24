'''
수 정렬하기 
'''

import sys

n = int(input())

num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    sys.stdout.write(str(i)+'\n')

'''
본 문제는 문제 자체는 쉽지만 속도 제한이 있어서
print와 input보다 빠른 sys를 사용하였다
'''
