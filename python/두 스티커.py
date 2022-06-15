H, W = map(int, input().split())
N = int(input())
board = list(list(map(int, input().split())) for _ in range(N))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        r1, c1 = board[i] # a 스티커
        r2, c2 = board[j] # b 스티커

        if ((r1 + r2) <= H and max(c1, c2) <= W) or ((c1 + c2) <= W and max(r1, r2) <= H):
            ans = max(ans, r1*c1 + r2*c2)
            # 스티커가 둘다 회전하지 않는 경우

        if ((r1 + c2) <= H and max(c1, r2) <= W) or ((c1 + r2) <= W and max(r1, c2) <= H):
            ans = max(ans, r1 * c1 + r2 * c2)
            # b 스티커가 회전한 경우

        if ((c1 + r2) <= H and max(r1, c2) <= W) or ((r1 + c2) <= W and max(c1, r2) <= H):
            ans = max(ans, r1 * c1 + r2 * c2)
            # a 스티커가 회전한경우

        if ((c1 + c2) <= H and max(r1, r2) <= W) or ((r1 + r2) <= W and max(c1, c2) <= H):
            ans = max(ans, r1 * c1 + r2 * c2)
            # a, b 둘다 회전한 경우
print(ans)