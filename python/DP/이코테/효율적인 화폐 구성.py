n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
# 10001이란 숫자는 m의 최대 값이 10000이기 때문이다
d[0] = 0
for i in range(n): 
    # i는 화폐의 종류마다 계산할수 있게함
    for j in range(array[i], m + 1):
        # j는 화폐를 지정하고 한가지 화폐를 모두 계산함
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]]+1)
            # d[j - array[i]] 는 현재 위치에서 화폐의 배수에 맞는 최솟 값을 
            # 뺀값으로 그 위치에 뺀 흔적이 있으면 그배수인 자신도 뺼수 있다는
            # 이론으로 만들어짐

if d[m] == 10001:
    print(-1)
else:
    print(d[m])


