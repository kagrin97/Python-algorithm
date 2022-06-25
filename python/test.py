import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
cow = list(map(int, input().split()))
joke = list(map(int, input().split()))


for jo in range(Q):
    a = 0
    cow[joke[jo]- 1] = cow[joke[jo]- 1] * -1
    for i in range(N):
        num = cow[i]
        for j in range(i+1,i+4):
                j = j % N
                num *= cow[j]
        a += num
    print(a)