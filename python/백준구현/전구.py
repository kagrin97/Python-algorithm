n, m = map(int, input().split())
state = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        state[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if state[i] == 1:
                state[i] = 0
            else:
                state[i] = 1
    elif a == 3:
        for i in range(b - 1, c):
            state[i] = 0
    elif a == 4:
        for i in range(b - 1, c):
            state[i] = 1

for i in state:
    print(i, end=" ")