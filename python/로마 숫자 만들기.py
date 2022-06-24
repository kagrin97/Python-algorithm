from itertools import combinations_with_replacement

n = int(input())
sa = set()

for i in combinations_with_replacement([1, 5, 10, 50], n):
    sa.add(sum(i))

print(len(sa))
