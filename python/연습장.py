A, B = map(int, input().split())
q = [(B, 1)]
result = -1
while q:
    x, cnt = q.pop(0)
    if x == A:
        result = cnt
        break

    if x % 2 == 0 and x / 2 >= A:
        q.append((x / 2, cnt + 1))
    elif x % 10 == 1 and x / 10 >= A:
        q.append((x // 10, cnt + 1))
    else:
        break

print(result)
