N = int(input())
homework = []
for _ in range(N):
    d, w = map(int, input().split())
    homework.append((d, w))

homework.sort()
print(homework)
can = []
date = homework[-1][0]
print(date)
answer = 0
while True:
    if date == 0:
        break
    while homework and homework[-1][0] >= date:
        can.append(homework.pop()[1])
    date -= 1
    if not can:
        continue
    can.sort()
    print(can)
    answer += can.pop()
print(answer)