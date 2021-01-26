import sys
from bisect import bisect_left, bisect_right

n = int(input())  # n_array의 길이
n_array = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_array = list(map(int, sys.stdin.readline().split()))


def find_number(n_array, left_value, right_value):
    right_index = bisect_right(n_array, right_value)

    left_index = bisect_left(n_array, left_value)

    return right_index - left_index


n_array.sort()

for i in m_array:
    count = find_number(n_array, i, i)
    print(count, end=' ')
