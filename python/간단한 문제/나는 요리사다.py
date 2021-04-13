cook = []
for _ in range(5):
    cook.append(sum(list(map(int, input().split()))))

max_point = max(cook)

for i in range(len(cook)):
    if cook[i] == max_point:
        print(i+1, end=' ')
        print(cook[i])


