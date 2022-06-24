N, C = map(int, input().split())
M = int(input())
info = []
for _ in range(M):
    info.append(list(map(int, input().split())))
info.sort(key=lambda x:x[1]) # 도착지점이 더 가까울수록 더 많은 택배 가능
temps = [C]*(N)
amount = 0

for i in range(len(info)):
    min_val = C + 1
    for j in range(info[i][0], info[i][1]):
        if temps[j] < min_val:
            min_val = temps[j]
    
    t = min(min_val, info[i][2])
    amount += t
    for j in range(info[i][0], info[i][1]):
        temps[j] -= t

print(amount)