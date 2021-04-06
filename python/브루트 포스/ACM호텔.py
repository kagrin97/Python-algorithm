t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    b = (n // h) + 1
    if a == 0: # 0일경우는 6층호텔에 6번쨰 손님이올경우
        b -= 1
        a = h # 가장 높은 층을 준다
    print(a*100+b)


    




