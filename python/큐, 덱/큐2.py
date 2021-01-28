import sys
from collections import deque

n = int(sys.stdin.readline())
deque = deque()

def push(queque, x):
    deque.append(x)

def pop(deque):
    if(not deque):
        return -1
    else:
        return deque.popleft()

def size():
    return len(deque)

def empty():
    if(not deque):
        return 1
    else:
        return 0

def front():
    if(not deque):
        return -1
    else:
        return deque[0]

def back():
    if(not deque):
        return -1
    else:
        return deque[-1]

for i in range(n):
    op = sys.stdin.readline().split()
    
    if(op[0] == "push"):
        push(deque, op[1])
    elif(op[0] == "pop"):
        print(pop(deque))
    elif(op[0] == "size"):
        print(size())
    elif(op[0] == "empty"):
        print(empty())
    elif(op[0] == "front"):
        print(front())
    elif(op[0] == "back"):
        print(back())