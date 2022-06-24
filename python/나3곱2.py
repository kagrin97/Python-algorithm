def check(x, b, A):
    b.remove(x)
    A.append(x)
    least_one = False
    if not b:
        return True
    if x * 2 in b:
        least_one = True
        return check(x * 2, b, A)
    if x % 3 == 0 and x // 3 in b:
        least_one = True
        return check(x // 3, b, A)
    if not least_one:
        return False

n = int(input())
n_list = list(map(int, input().split()))

for i in range(n):
    A = []
    if check(n_list[i], n_list.copy(), A):
        print(*A)
        break
