import sys
import itertools
input = sys.stdin.readline

ki = []
for i in range(9):
    ki.append(int(input()))

find = sum(ki) - 100
nCr = itertools.combinations(ki, 2)

for i in nCr:
    if sum(i) == find:
        a, b = i[0], i[1]
        ki.remove(a)
        ki.remove(b)
        break
ki = sorted(ki)

for i in ki:
    print(i)
