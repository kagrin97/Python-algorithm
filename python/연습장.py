import heapq
import sys 
import bisect

n = int(sys.stdin.readline())
x = []
answers = []

for _ in range(n):
    bisect.insort(x, int(sys.stdin.readline()))
    if len(x) % 2 == 0:
        answers.append(x[int(len(x) / 2) - 1])
    else:
        answers.append(x[int(len(x) / 2)])

for i in answers:
    print(i)