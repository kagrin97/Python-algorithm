t = int(input())
a, b, c = 0, 0, 0
at, bt, ct = 300, 60, 10

while t >= at:
    t -= at
    a += 1
while t >= bt:
    t -= bt
    b += 1
while t >= ct:
    t -= ct
    c += 1

if t != 0:
    print(-1)
else:
    print(a,b,c)
    