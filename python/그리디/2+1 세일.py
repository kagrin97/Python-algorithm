N = int(input())
ware = []
for i in range(N):
  ware.append(int(input()))
ware.sort(reverse=True)

result=0
for i in range(2, len(ware), 3):
  result += ware[i]

print(sum(ware) - result)


