import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
k = int(input())
for i in range(k):
    answer = 0
    i, j, x, y = map(int, input().split())
    temp = arr[i-1:x]
    for t in temp:
        answer += sum(t[j-1:y])
    print(answer)
