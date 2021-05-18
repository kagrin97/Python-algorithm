N = int(input())
point = []
for _ in range(N):
    point.append(int(input()))

p_len = len(point)
point_r = list(reversed(point))
cnt = 0

for i in range(len(point_r)-1):
    
    if point_r[i] <= point_r[i+1]:
        while point_r[i] <= point_r[i+1]:
            point_r[i+1] -= 1
            cnt += 1
print(cnt)
