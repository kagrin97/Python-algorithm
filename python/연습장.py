import sys

n = int(sys.stdin.readline())

array = [0,0,0]
for i in range(n):
    array.append(int(sys.stdin.readline()))

table = [0 for _ in range(len(array))]
for i in range(3, n+3):
    table[i] = max(table[i-1], table[i-2] + array[i], 
    table[i-3] + array[i-1] + array[i])


print(table[n+2])




