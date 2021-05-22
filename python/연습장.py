N, L = map(int, input().split())
water = list(map(int, input().split()))
water.sort()
cnt = 0
for i in range(N):
    tape = [i for i in range(water[i], water[i]+L)]

    for t in tape:
        if t in water:
            water.remove(t)
    cnt += 1

print(cnt)
