import sys
input = sys.stdin.readline

n = int(input())
x = int(input())

matrix = [[0] * (n + 1) for _ in range(n + 1)]
virus = [0] * (n + 1)
for i in range(x):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

count = 0

def dfs(x):
    global count
    virus[x] = 1
    for i in range(1, n + 1):
        if virus[i] == 0 and matrix[x][i]:
            count += 1
            dfs(i)


dfs(1)
print(count)



