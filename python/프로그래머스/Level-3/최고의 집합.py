from collections import deque
def solution(n, s):
    if n > s:
        return [-1]
    [even, again] = divmod(s, n)
    answer = [even] * n

    for i in range(again):
        answer[i] += 1
    return sorted(answer)

n = 4
s = 15
print(solution(n, s))

'''
이문제에서 n개의 자연수의 곱이 가장 높게 될려면
n개의 숫자가 모두 비슷한 숫자여야 곱이 가장 높게 나온다
그래서 n개의 숫자를 평평하게 만든다 3,3,3,3 (6번째 줄)
그리고 나머지 숫자들(s가 되기위한 나머지 값) 을 하나씩
1씩 n개의 숫자들에 더해주고 정렬해주면 문제가 풀린다
'''