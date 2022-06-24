x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i - 1] + 1
    # 1을 뺴는 경우 
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        # 2로도 나눠지고 1로뺀 수랑 비교 후 갱신
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

