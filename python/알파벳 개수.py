# import sys
# input = sys.stdin.readline
s = list(input())
alpha = [0] * 26


for i in s:
    a = s.count(i)
    b = ord(i) - 97
    alpha[b] = a

for i in alpha:
    print(i, end=" ")




