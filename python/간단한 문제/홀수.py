num = []
for _ in range(7):
    num.append(int(input()))

odd = []
for i in num:
    if i % 2 != 0:
        odd.append(i)

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)