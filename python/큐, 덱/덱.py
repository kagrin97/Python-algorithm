from collections import deque
import sys

n = int(sys.stdin.readline())
dq = deque()
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        dq.appendleft(order[1])
    elif order[0] == 'push_back':
        dq.append(order[1])
    elif order[0] == 'pop_front':
        if not dq:
            print(-1)
        else:
            remove = dq.popleft()
            print(remove)
    elif order[0] == 'pop_back':
        if not dq:
            print(-1)
        else:
            remove = dq.pop()
            print(remove)
    elif order[0] == 'size':
        print(len(dq))
    elif order[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif order[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])
