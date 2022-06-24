a = int(input())

arrary = list(map(int, input().split()))

dp_one = [1] * a
dp_two = [1] * a
result = [0] * a
# 정방향, 역방향, 결과값 리스트 생성
for i in range(a):
    for j in range(i):
        if arrary[j] < arrary[i]:
            dp_one[i] = max(dp_one[i], dp_one[j] + 1)
        
for i in range(a-1, -1, -1):
    for j in range(a-1, i, -1):
        if arrary[j] < arrary[i]:
            dp_two[i] = max(dp_two[i], dp_two[j] + 1)

for i in range(a):
    result[i] = dp_one[i] + dp_two[i] -1
# 정방향, 역방향 결과 값을 더하고 -1을 한다(두번 더했기 때문)
print(max(result))
    