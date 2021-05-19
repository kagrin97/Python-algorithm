from itertools import permutations
T = int(input())

for _ in range(T):
    N = int(input())
    tree = list(map(int, input().split()))
    tree.sort()

    max_val = 0
    for i in range(2, N):
        max_val = max(max_val, abs(tree[i] - tree[i-2]))
    
    print(max_val)