from collections import deque

def solution(n, words):
    ans = [0, 0]

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            ans[0] = (i % n) + 1
            ans[1] = (i // n) + 1
            print(i, n)
            break
    return ans

n = 2
w = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, w))