count = 0
for i in range(8):
    mal = list(map(str, input().split()))
    if i % 2 == 0:
        for idx, m in enumerate(mal[0]):
            if idx % 2 == 0 and m == 'F':
                count += 1
    else:
        for idx, m in enumerate(mal[0]):
            if idx % 2 != 0 and m == 'F':
                count += 1
print(count)
