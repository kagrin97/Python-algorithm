l, p = map(int, input().split())
num = l * p
news = [list(map(int, input().split()))]

for i in range(5):
    print(news[0][i] - num, end=' ')