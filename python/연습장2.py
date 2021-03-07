from copy import deepcopy

a = [2, 3, 3, 6, 1, 3, 4]

s = deepcopy(a)
s[0] = 10
print(a, s)