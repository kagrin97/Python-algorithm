t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    a = str(n % h)
    b = str((n // h) + 1)
    print(a+'0'+b)


    




