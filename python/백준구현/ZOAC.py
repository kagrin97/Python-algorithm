import sys
input = sys.stdin.readline

S = list(input().rstrip())
result = ['']*len(S)


def func(arr, start):
    if not arr:
        return
    min_alpha = min(arr)
    min_idx = arr.index(min_alpha)
    result[start+min_idx] = min_alpha
    print("".join(result))
    func(arr[min_idx+1:], start+min_idx+1)
    func(arr[:min_idx], start)


func(S, 0)