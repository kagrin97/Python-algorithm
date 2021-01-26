import sys

n = int(input())
n_array = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_array = list(map(int, sys.stdin.readline().split()))


def find_number(n_array, number, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0
    if n_array[mid] > number:
        return find_number(n_array, number, start, mid-1)
    elif n_array[mid] < number:
        return find_number(n_array, number, mid + 1, end)
    else:
        return 1


n_array.sort()
for i in m_array:
    print(find_number(n_array, i, 0, n-1))
