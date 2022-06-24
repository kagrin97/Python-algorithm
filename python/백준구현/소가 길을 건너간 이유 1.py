n = int(input())
log = {}
cnt = 0
for i in range(n):
    cow, location = map(int, input().split())
    if cow in log:
        if log[cow] != location:
            cnt += 1
            log[cow] = location
    else:
        log[cow] = location

print(cnt)