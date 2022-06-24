s = list(map(int, input().split()))
num = 0

for i in s:
    num = num + (i**2)

print(num % 10)