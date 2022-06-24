
E, S, M = map(int, input().split())
E1, S1, M1 = 0, 0, 0
cnt = 0

while E != E1 or S != S1 or M != M1:
    cnt += 1
    if E1 == 15:
        E1 = 0
    if S1 == 28:
        S1 = 0
    if M1 == 19:
        M1 = 0

    E1 += 1
    S1 += 1
    M1 += 1
print(cnt)