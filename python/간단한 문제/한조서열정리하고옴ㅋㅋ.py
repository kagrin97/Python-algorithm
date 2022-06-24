import sys
input = sys.stdin.readline

N = int(input())
hanzo = list(map(int, input().split()))
max_val = 0

for i in range(N):
  cnt = 0
  for j in range(i+1, N):
    if hanzo[i] > hanzo[j]:
      cnt += 1
    else:
      break
  max_val = max(max_val, cnt)

print(max_val)