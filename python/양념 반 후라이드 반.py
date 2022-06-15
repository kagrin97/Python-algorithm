a, b, c, x, y = map(int, input().split())
ans = 0

if (a + b) // 2 > c:
    min_val = min(x, y)
    ans += min_val * 2 * c
    x -= min_val
    y -= min_val
    if x != 0:
        if c * 2 > a:
            ans += a * x
        else:
            ans += c * 2 * x
    if y != 0:
        if c * 2 > b:
            ans += b * y
        else:
            ans += c * 2 * y
else:
    ans += a * x
    ans += b * y
print(ans)