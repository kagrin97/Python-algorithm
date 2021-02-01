n = int(input())

array = list(map(int, input().split()))
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])

'''
개미전사는 2가지 경우가 존재하는데 현재 식량 창고를 제외하고 터는 방법과
현재 식량 창고를 포함하고 터는 방법 이있다 그중 최선을 고르면 됨
점화식 : d[i] = max(d[i - 1], d[i - 2] + array[i])

