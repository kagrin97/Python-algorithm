import sys
n, c = map(int, sys.stdin.readline().rstrip("\n").split())
m = int(sys.stdin.readline().rstrip("\n"))
nums = []
temps = [c]*(n)
for _ in range(m):
    nums.append(list(map(int, sys.stdin.readline().rstrip("\n").split())))
nums = sorted(nums, key=lambda x:x[1])
print(temps)