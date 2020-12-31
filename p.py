n, k = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
count = 0
array.sort(reverse=True)

for i in array:
    if k >= i:
        count += k // i
        k %= i

print(count)
