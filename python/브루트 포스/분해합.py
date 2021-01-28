n = int(input())

for num in range(1, n + 1):
    num_list = list(map(int, str(num)))
    result = num + sum(num_list)
    if result == n:
        print(num)
        break
    elif num == n:
        print(0)