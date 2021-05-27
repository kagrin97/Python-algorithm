N = int(input())
flower = []
for _ in range(N):
    arr = list(map(int, input().split()))
    start = arr[0] * 100 + arr[1]
    end = arr[2] * 100 + arr[3]
    flower.append([start, end])
flower.sort()
count = 0
memo = 0
start = 301
maxdate = 0
for i in range(N):
    if start > 1130:
        break
    if flower[i][0] <= start and flower[i][1] > start:
        if memo != start:
            memo = start
            count += 1
        
        if maxdate < flower[i][1]:
            maxdate = flower[i][1]
    else:
        if memo == start:
            if flower[i][0] <= maxdate and flower[i][1] > maxdate:
                start = maxdate
                memo = start
                maxdate = flower[i][1]
                count += 1
        else:
            if start < flower[i][0]:
                count = 0
                break
if maxdate <= 1130:
    count = 0
print(count)