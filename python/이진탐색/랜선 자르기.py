import sys

array = []
n, m = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    array.append(int(sys.stdin.readline()))

start = 1
end = max(array)


while (start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        total += x // mid

    if total >= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)
